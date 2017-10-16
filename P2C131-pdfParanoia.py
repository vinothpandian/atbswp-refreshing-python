#! python3

import PyPDF2, os, sys

if len(sys.argv) == 4:
	PDF_FOLDER = sys.argv[1]
	OPTION = sys.argv[2]
	PASSWORD = sys.argv[3]
else:
	print("Run the file as P2C131-pdfParanoia.py [Folder] [encrypt|decrypt] [password]")
	sys.exit()

FOLDER_NAME = "P2C13"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

if OPTION == "encrypt":
	encrypt(PDF_FOLDER, PASSWORD)
elif OPTION == "decrypt":
	decrypt(PDF_FOLDER, PASSWORD)
else:
	print("Enter option as encrypt or decrypt (case-sensitive)")
	sys.exit()

def encrypt(folder, password):
	for folderName, subFolders, fileNames in os.walk(folder):
		for file in fileNames:
			if file.endswith(".pdf"):
				filePath = os.path.join(folderName, file)
				print("Reading and encrypting %s...." %filePath)

				pdfFile = open(filePath, "rb")
				pdfReader = PyPDF2.PdfFileReader(pdfFile)

				if !pdfReader.isEncrypted:
					pdfWriter = PyPDF2.PdfFileWriter()
				
					for page in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(page))

					pdfWriter.encrypt(password)
					encFileName = filePath[:-4]+"_encrypted.pdf"
					encryptedFile = open(encFileName, "wb")
					pdfWriter.write(encryptedFile)
					print("Encrypted to %s" %encFileName)

					pdfFile.close()
					print("Deleting old file %s....\n\n" % filePath)
					#os.unlink(filePath)
				else:
					print("File %s is already in encrypted state\n\n" %pdfFile)

					print("Done")

def decrypt(folder, password):
	for folderName, subFolders, fileNames in os.walk(folder):
		for file in fileNames:
			if file.endswith(".pdf"):
				filePath = os.path.join(folderName, file)
				print("Reading and decrypting %s...." %filePath)

				pdfFile = open(filePath, "rb")
				pdfReader = PyPDF2.PdfFileReader(pdfFile)

				if pdfReader.isEncrypted:
					pdfWriter = PyPDF2.PdfFileWriter()
				
					for page in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(page))

					pdfWriter.encrypt(password)
					encFileName = filePath[:-4]+"_decrypted.pdf"
					encryptedFile = open(encFileName, "wb")
					pdfWriter.write(encryptedFile)
					print("Encrypted to %s" %encFileName)

					pdfFile.close()
					#os.unlink(filePath)
				else:
					print("File %s is already not in encrypted state\n\n" %pdfFile)
					print("Done")
