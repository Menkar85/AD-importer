from pyad import aduser, adcontainer
from pyad.pyad import set_defaults
from copy import deepcopy
import logging

from utils.xlsxutils import write_excel_data

FIRST_RUN = True
TARGET = None

logger = logging.getLogger(__name__)

def is_user_exists(cn):
    """
    Define whether a user exists in the Active Directory.
    Args:
        cn(str): Username to check.

    Returns:
        bool: True if the user exists in the Active Directory.

    """
    try:
        aduser.ADUser.from_cn(cn)
        return True
    except Exception as e:
        return False


def get_or_create_ou(ou_name, parent_dn):
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
