#! python

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


def encrypt(folder, password):
    for folderName, subFolders, fileNames in os.walk(folder):
        for file in fileNames:
            if file.endswith(".pdf"):
                file_path = os.path.join(folderName, file)
                print("Reading and encrypting %s...." % file_path)

                pdf_file = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                if not pdf_reader.isEncrypted:
                    pdf_writer = PyPDF2.PdfFileWriter()

                    for page in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page))

                    pdf_writer.encrypt(password)
                    enc_file_name = file_path[:-4] + "_encrypted.pdf"
                    encrypted_file = open(enc_file_name, "wb")
                    pdf_writer.write(encrypted_file)
                    print("Encrypted to %s" % enc_file_name)

                    pdf_file.close()
                    print("Deleting old file %s....\n" % file_path)
                # os.unlink(file_path)
                else:
                    print("File %s is already in encrypted state\n" % file_path)
                    print("Done")


def decrypt(folder, password):
    for folderName, subFolders, fileNames in os.walk(folder):
        for file in fileNames:
            if file.endswith(".pdf"):
                file_path = os.path.join(folderName, file)
                print("Reading and decrypting %s...." % file_path)

                pdf_file = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                if pdf_reader.isEncrypted:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    if pdf_reader.decrypt(PASSWORD) == 0:
                        print("Password incorrect.. Cannot decrypt file %s" % file_path)
                    else:

                        for page in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page))

                        dec_file_name = file_path[:-4] + "_decrypted.pdf"
                        dec_file_name = dec_file_name.replace("_encrypted", "")
                        encrypted_file = open(dec_file_name, "wb")
                        pdf_writer.write(encrypted_file)

                        print("Decrypted to %s\n" % dec_file_name)
                        pdf_file.close()

                else:
                    print("File %s is not in encrypted state\n" % file_path)
                    print("Done")


if OPTION == "encrypt":
    encrypt(PDF_FOLDER, PASSWORD)
elif OPTION == "decrypt":
    decrypt(PDF_FOLDER, PASSWORD)
else:
    print("Enter option as encrypt or decrypt (case-sensitive)")
    sys.exit()
