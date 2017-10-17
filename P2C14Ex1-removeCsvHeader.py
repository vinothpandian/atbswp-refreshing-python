#! python

import csv, os

FOLDER_NAME = "P2C14"
CSV_FOLDER = "headerRemoved"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

os.makedirs(CSV_FOLDER, exist_ok=True)

for file in os.listdir("."):
    if file.endswith(".csv"):
        print("Deleting header row from %s...." % file)
        csvFile = open(file)
        csvReader = csv.reader(csvFile)

        csvData = []

        for row in csvReader:
            if csvReader.line_num != 1:
                csvData.append(row)

        csvWriteFile = open(os.path.join(CSV_FOLDER, file), "w", newline="")
        csvWriter = csv.writer(csvWriteFile)

        for data in csvData:
            csvWriter.writerow(data)

        csvWriteFile.close()
        csvFile.close()

print("New files are stored in %s folder...." % CSV_FOLDER)
print("Done")