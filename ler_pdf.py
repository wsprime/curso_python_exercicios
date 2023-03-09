# Primeiro utilize no terminal de comandos:
# pip install PyPDF2

from PyPDF2 import PdfReader

reader = PdfReader("pdf_sample_2.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)