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
	# Ищем блоки текста, начинающиеся с "Стр.:" и содержащие пары "Ключ: Значение"
	pattern = re.compile(r"Стр\.: (\d+)(.*?)(?=\n\n|$)", re.DOTALL)
	matches = pattern.findall(text)
	
	data_dict = {}
	
	for match in matches:
		page_number, page_content = match
		page_data = {"Стр.": int(page_number)}
		
		# Ищем пары "Ключ: Значение" на странице
		key_value_pattern = re.compile(r"([^:\n]+):(.+?)(?:(?=\n[^:\n]+:)|\Z)", re.DOTALL)
		key_value_matches = key_value_pattern.findall(page_content)
		
		for key, value in key_value_matches:
			page_data[key.strip()] = value.strip()
		
		data_dict[int(page_number)] = page_data
	
	return data_dict


# Пример использования
file_path = '810abb0c-4cbf-467b-b319-57896a28f42c.pdf'
pdf_text = read_pfd(file_path)
parsed_data = parse_text_with_regex(pdf_text)

# Вывести результат
for page_number, data in parsed_data.items():
	print(f"Страница: {page_number}")
	print(data)
	print("\n")