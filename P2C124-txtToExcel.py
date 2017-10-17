#! python

import openpyxl, os

FOLDER_NAME = "./P2C12/"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

TEXTFILE_FOLDER = "txtFiles2convert"

print("Creating workbook....")
workbook = openpyxl.Workbook()
sheet = workbook.get_active_sheet()
col = 0

print("Finding the files in %s folder...." % TEXTFILE_FOLDER)
for file in os.listdir(TEXTFILE_FOLDER):
    if file.endswith(".txt") :
        col += 1
        print("Reading text file \"%s\" and writing it to excel sheet...." % file)
        txtFile = open(os.path.join(TEXTFILE_FOLDER, file))
        content = txtFile.readlines()
        row = 0
        for line in content:
            row += 1
            sheet.cell(row=row, column=col).value = line

print("Saving the excel sheet....")
workbook.save("txtToExcel.xlsx")
workbook.close()

print("Done")