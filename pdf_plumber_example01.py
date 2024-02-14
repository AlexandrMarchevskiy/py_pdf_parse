import pdfplumber


def extract_table(pdf_path, page_num, table_num):
    pdf = pdfplumber.open(pdf_path)
    table_page = pdf.pages[page_num]
    table = table_page.extract_tables()[table_num]
    return table


# print(extract_table('810abb0c-4cbf-467b-b319-57896a28f42c.pdf', 0, 2)[4:])

def format_table_0_0(table):
    formatted_dict = {}

    for entry in table:
        for item in entry.split('\n'):
            if ': ' in item:
                key, value = item.split(': ', 1)
            else:
                key, value = item, ''

            formatted_dict[key] = value

    return formatted_dict



table_data = extract_table('810abb0c-4cbf-467b-b319-57896a28f42c.pdf', 0, 0)
formatted_table = format_table_0_0(table_data[0])


print(formatted_table)

def format_0_2_table(table):
    header = table[0]
    data = table[1:]

    formatted_dicts = []

    for row in data:
        formatted_dict = {key: value for key, value in zip(header, row) if value is not None}
        formatted_dicts.append(formatted_dict)

    return formatted_dicts


table_data = extract_table('810abb0c-4cbf-467b-b319-57896a28f42c.pdf', 0, 2)[4:]
print(*format_0_2_table(table_data))