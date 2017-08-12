#! python3

import re,os, shutil

FOLDER = 'P2C93-NumberedFiles'

nameRegex = re.compile(r'(\d+)')

def listGaps(folder, gapFile):

    storeGapFile = open(os.path.join(folder, gapFile),'w')

    num = 1
    for fileName in os.listdir(folder):

        oldLocation = os.path.join(folder, fileName)
        match = nameRegex.search(fileName)

        if match == None:
            continue

        fileNum = str(num).rjust(3,'0')
        if match.group(1) == fileNum:
            num += 1
            continue
        else:
            print('Found gap at %s' %fileNum)
            storeGapFile.write('Gap at file : %s\n' %fileNum)
            num += 2

    storeGapFile.close()

def fillGaps(folder):

    num = 1
    for fileName in os.listdir(folder):

        oldLocation = os.path.join(folder, fileName)
        match = nameRegex.search(fileName)

        if match == None:
            continue

        fileNum = str(num).rjust(3,'0')
        if match.group(1) == fileNum:
            num += 1
            continue
        else:
            newLocation = nameRegex.sub(fileNum, oldLocation)
            print('Rename %s to %s' %(oldLocation, newLocation))
            #shutil.move(oldLocation, newLocation)
            num += 1

listGaps(FOLDER, 'gaps.txt')
fillGaps(FOLDER)
