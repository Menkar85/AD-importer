import openpyxl
import transliterate


def get_excel_data(path, *, has_headers=True):
    try:
        wb = openpyxl.load_workbook(path)
        sheet = wb.active
    except Exception as e:
        return {'error': e}

    if has_headers and sheet.max_row > 0:
        headers = next(sheet.iter_rows(min_row=1, values_only=True))
    elif sheet.max_row > 0:
        headers = []
    else:
        raise ValueError("Excel book has no data!")

    start_row = 2 if has_headers else 1
    data_rows = sheet.iter_rows(min_row=start_row, values_only=True)
    return {
        'headers': headers,
        'data': data_rows
    }


def build_import_data(input_dict, upn, mail_domain=None):
    user_data = []
    if not mail_domain:
        mail_domain = upn
    for row in input_dict['data']:
        user = {
            'cn': f"{transliterate.translit(row)}{row[2]}",
            'givenName': row[0],
            'sn': row[1],
            'displayName': f"{row[0]} {row[1]}",
            'password': row[3],
            'userPrincipalName': f"{str(transliterate.translit(row))+str(row[2])}@{upn}",
            'mail': f"{str(transliterate.translit(row))+str(row[2])}@{mail_domain}",
            'telephoneNumber': row[4],
            'description': row[5]
        }
        user_data.append(user)
    return user_data


def write_excel_data(path, data):
    wb = openpyxl.Workbook()
    sheet = wb.create_sheet('result')
    # TODO: complete data writing into result file
