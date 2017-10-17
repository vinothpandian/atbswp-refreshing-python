#! python

import PyPDF2, os

FOLDER_NAME = "./P2C13/"
PDF_FOLDER = "PDFfiles"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

print("Scanning \"%s\" folder for pdf files...." % PDF_FOLDER)
files = [] 
for file in os.listdir(PDF_FOLDER):
	if file.endswith(".pdf"):
		files.append(file)

files.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for file in files:
	print("Combining file \'%s\'..." % file)
	pdfFile = open(os.path.join(PDF_FOLDER, file),"rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	for i in range(1, pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(i))

print("Saving file....")
pdfWriteFile = open("combined.pdf", "wb")
pdfWriter.write(pdfWriteFile)
pdfWriteFile.close()

print("Done")

