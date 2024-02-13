from pypdf import PdfReader


def read_pfd(file_path):
	with open(file_path, 'rb') as file:
		reader = PdfReader(file)
		number_of_pages = len(reader.pages)
		
		count = 1
		text = ''
		for page_num in range(number_of_pages):
			page = reader.pages[page_num]
			text += page.extract_text()
			print(f'СТРАНИЦА {count}:\n{page.extract_text()}')
			count += 1
			
	return text

# file_path = '810abb0c-4cbf-467b-b319-57896a28f42c.pdf'
# pdf_text = read_pfd(file_path)
# print(pdf_text)

