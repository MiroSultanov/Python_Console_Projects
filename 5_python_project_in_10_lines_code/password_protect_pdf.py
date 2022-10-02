from pyPDF2 import PdfFileWritter, PdfFileReader
import getpass

pdfwritter = PdfFileWritter()
pdf = PdfFileReader("1.pdf")

for page_num in range(pdf.numPages):
    pdfwritter.addPage(pdf.getPage(page_num))

passw = getpass.getpass(prompt="Enter Password: ")
pdfwritter.encrypt(passw)

with open("ho.pdf", "wb") as f:
    pdfwritter.write(f)
