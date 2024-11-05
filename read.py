from PyPDF2 import PdfReader

reader = PdfReader("Intro/byte-of-python.pdf")
page = reader.pages[1]
print(page.extract_text())