import re
from pypdf import PdfReader


def read_pfd(file_path):
	with open(file_path, 'rb') as file:
		reader = PdfReader(file)
		number_of_pages = len(reader.pages)
		
		text = ''
		for page_num in range(number_of_pages):
			page = reader.pages[page_num]
			text += page.extract_text()
	
	return text


def parse_text_with_regex(text):
	pattern = re.compile(r"Стр\.: (\d+)(.*?)(?=\n\n|$)", re.DOTALL)
	matches = pattern.findall(text)

	data_dict = {}

	for match in matches:
		page_number, page_content = match
		page_data = {"Стр.": int(page_number)}

		key_value_pattern = re.compile(r"([^:\n]+):(.+?)(?:(?=\n[^:\n]+:)|\Z)", re.DOTALL)
		key_value_matches = key_value_pattern.findall(page_content)

		for key, value in key_value_matches:
			page_data[key.strip()] = value.strip()

		data_dict[int(page_number)] = page_data

	return data_dict

def parse_text(text):

	regex_pattern = r'([^\:]+):\s*([^А-Яа-я\n]+)'
	matches = re.findall(regex_pattern, text)


	parsed_dict = {key.strip(): value.strip() for key, value in matches}

	return parsed_dict


file_path = '810abb0c-4cbf-467b-b319-57896a28f42c.pdf'
pdf_text = read_pfd(file_path)
print(pdf_text)
# result_dict = parse_text(pdf_text)
# parsed_data = parse_text_with_regex(pdf_text)
#
#
# for page_number, data in parsed_data.items():
# 	print(f"Страница: {page_number}")
# 	print(data)
# 	print("\n")
# for key, value in result_dict.items():
# 	print(f"{key}: {value}")
