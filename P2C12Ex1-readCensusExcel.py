#! python
import openpyxl, os, pprint

FOLDER_NAME = "./P2C12/"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

print("opening the workbook.............")

workbook = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = workbook.get_sheet_by_name("Population by Census Tract")

countyData = {}

print("Reading and processing.........")
for i in range(2, sheet.max_row + 1 ):
    state = sheet['B'+str(i)].value
    county = sheet['C'+str(i)].value
    pop = sheet['D'+str(i)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    countyData[state][county]["tracts"] += 1
    countyData[state][county]["pop"] += pop

print("Writing the result........")
reportFile = open("censusReport.py", 'w')
reportFile.write("data = " + pprint.pformat(countyData))
reportFile.close()

print("Success......")
