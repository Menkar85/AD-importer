from pyad import aduser, adcontainer
from pyad.pyad import set_defaults
from copy import deepcopy
import logging

from utils.xlsxutils import write_excel_data

FIRST_RUN = True
TARGET = None

logger = logging.getLogger(__name__)

def is_user_exists(cn):
    """Check if a user exists in the Active Directory.
    
    Args:
        cn (str): Username to check.

    Returns:
        bool: True if the user exists in the Active Directory, False otherwise.
    """
    try:
        aduser.ADUser.from_cn(cn)
        return True
    except Exception as e:
        return False


def get_or_create_ou(ou_name, parent_dn):
    """Get an existing OU or create it if it doesn't exist.
    
    Args:
        ou_name (str): Name of the organizational unit to find or create.
        parent_dn (str): Distinguished name of the parent container.
        
    Returns:
        ADContainer: The found or newly created organizational unit.
        
    Note:
        This function uses global variables FIRST_RUN and TARGET to track
        the first run and target OU name for logging purposes.
    """
    global FIRST_RUN
    try:
        ou = adcontainer.ADContainer.from_dn(f'OU={ou_name},{parent_dn}')
        if ou_name == TARGET and FIRST_RUN:
            FIRST_RUN = False
        logger.info(f'OU {ou} exists.')
        return ou
    except Exception as e:
        parent_container = adcontainer.ADContainer.from_dn(parent_dn)
        ou = parent_container.create_container(ou_name)
        logger.info(f'OU {ou} was created.')
        return ou


def get_destination_user_ou(destination_ou, domain):
    """Get or create the destination organizational unit for users.
    
    Parses the destination OU path and creates any missing OUs in the hierarchy.
    
    Args:
        destination_ou (str): Path to the destination OU (e.g., "OU1/OU2/OU3").
        domain (str): Domain name (e.g., "example.com").
        
    Returns:
        ADContainer: The destination organizational unit where users will be created.
        
    Note:
        This function uses global variable TARGET to track the target OU name.
    """
    global TARGET
    ou_list = [value for value in destination_ou.split("/") if value]
    parent_dn = f"DC={',DC='.join(domain.split('.'))}"
    if ou_list:
        TARGET = ou_list[-1]
        for i in range(len(ou_list)):
            parent = get_or_create_ou(ou_list[i], parent_dn)
            parent_dn = parent.dn
        user_destination_ou = parent
    else:
        user_destination_ou = adcontainer.ADContainer.from_dn(parent_dn)
    logger.info(f"Users to be created in {user_destination_ou}")
    return user_destination_ou


def create_ad_user(ou, data):
    """Create a new user in Active Directory.
    
    Creates a new AD user with the specified attributes and settings.
    Checks for duplicate usernames and handles errors appropriately.
    
    Args:
        ou (ADContainer): The organizational unit where the user will be created.
        data (dict): Dictionary containing user attributes including:
            - cn: Common name (username)
            - displayName: Display name
            - userPrincipalName: User principal name
            - givenName: First name
            - sn: Surname
            - mail: Email address
            - telephoneNumber: Phone number
            - password: Initial password
            
    Raises:
        ValueError: If a duplicate username is detected on the first run.
        Exception: Any other error that occurs during user creation.
        
    Note:
        This function uses global variable FIRST_RUN to track duplicate detection
        and force password change on first login for new users.
    """
    try:
        if is_user_exists(data['cn']):
            if FIRST_RUN:
                logger.warning(f"Duplicate username: '{data['cn']}' detected. Usernames should be unique within domain.")
                raise ValueError("Duplicate detected")
            logger.info(f"User '{data['cn']}' already exists.")
            return
        else:
            new_user = aduser.ADUser.create(name=data['cn'], container_object=ou, password=data['password'])
            new_user.update_attributes({
                'displayName': data['displayName'],
                'userPrincipalName': data['userPrincipalName'],
                'givenName': data['givenName'],
                'sn': data['sn'],
                'mail': data['mail'],
                'telephoneNumber': str(data['telephoneNumber'])
            })
            new_user.force_pwd_change_on_login()
            logger.info(f"Created user with username: '{data['cn']}'")
    except Exception as e:
        logger.critical(f"Unable to create user due to following error {e}")
        raise e


def import_ad_users(
        ad_server,
        destination_ou,
        username,
        password,
        protocol,
        data,
        result_path
):
    """Import multiple users into Active Directory.
    
    Main function that orchestrates the bulk import of users into AD.
    Sets up AD connection, processes user data, creates users, and logs results.
    
    Args:
        ad_server (str): Active Directory server hostname or IP address.
        destination_ou (str): Path to the destination organizational unit.
        username (str): AD username for authentication.
        password (str): AD password for authentication.
        protocol (str): Connection protocol ('LDAP' or 'LDAPS').
        data (list): List of dictionaries containing user data to import.
        result_path (str): Path where the results Excel file will be saved.
        
    Returns:
        int: Number of errors that occurred during the import process.
        
    Note:
        This function processes each user in the data list, creates them in AD,
        and tracks success/failure for each operation. Results are written to
        an Excel file with status information for each user.
    """
    set_defaults(
        ldap_server=ad_server,
        username=username,
        password=password,
        ssl=protocol == 'LDAPS'
    )
    errors = 0
    result_data = deepcopy(data)
    domain = '.'.join(ad_server.split('.')[1:])
    target_ou = get_destination_user_ou(destination_ou, domain)
    for i in range(len(data)):
        try:
            create_ad_user(target_ou, data[i])
            result_data[i]['done'] = 'Y'
            result_data[i]['errors'] = 'None'
        except Exception as e:
            errors += 1
            result_data[i]['done'] = 'N'
            result_data[i]['errors'] = str(e)
    write_excel_data(result_path, result_data)
    return errors
