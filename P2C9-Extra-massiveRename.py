#! python3

import re,os, shutil

FOLDER = 'P2C83-RegexSearch'

# nameRegex = re.compile(r'\s\(+(\d*)\)+')
nameRegex = re.compile(r'(\d+)')

def massiveRename(folder):

    for fileName in os.listdir(folder):
        oldLocation = os.path.join(folder, fileName)
        match = nameRegex.search(fileName)

        if match == None:
            continue

        fileName = nameRegex.sub(match.group(1), fileName)
        newLocation = os.path.join(folder, fileName)
        print('Renamed to %s' %newLocation)
        shutil.move(oldLocation, newLocation)



massiveRename(FOLDER)
