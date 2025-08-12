import openpyxl
from openpyxl.styles import Font, Alignment
import transliterate


def get_excel_data(path, *, has_headers=True) -> dict:
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
    data_rows = list(sheet.iter_rows(min_row=start_row, values_only=True))
    return {
        'headers': headers,
        'data': data_rows
    }


def build_import_data(input_dict, upn, mail_domain=None) -> list[dict]:
    user_data = []
    if not mail_domain:
        mail_domain = upn
    for row in input_dict['data']:
        if row[1] is not None:
            translit_name = str(transliterate.translit(row[1], language_code='ru', reversed=True))
            cname = translit_name + str(row[2] or '')
            user = {
                'cn': cname,
                'givenName': row[0],
                'sn': row[1],
                'displayName': f"{row[0]} {row[1]}",
                'password': row[3],
                'userPrincipalName': f"{cname}@{upn}",
                'mail': f"{cname}@{mail_domain}",
                'telephoneNumber': row[4],
                'description': row[5]
            }
            user_data.append(user)
        else:
            break
    return user_data


def write_excel_data(path, data: list[dict]):
    wb = openpyxl.Workbook()
    sheet = wb.active
    header_font = Font(name='Times New Roman', size=14, bold=True, underline="single")
    body_font = Font(name='Times New Roman', size=14, bold=False)
    center_alignment = Alignment(horizontal="center")
    # headers
    for column in range(len(data[0])):
        sheet.cell(row=1, column=column + 1, value=list(data[0].keys())[column])
        sheet[1][column].font = header_font
        sheet[1][column].alignment = center_alignment

    # data
    for row in range(len(data)):
        for column in range(len(data[row])):
            sheet.cell(row + 2, column + 1, list(data[row].values())[column])
            sheet[row + 2][column].font = body_font
            sheet[row + 2][column].alignment = center_alignment
    wb.save(path)
