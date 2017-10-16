#! python

import os

FOLDER = 'D:\Studies'

def massiveFileSearch(folder, fileSizeinMB):

    sizeLimit = fileSizeinMB*1024**2

    for folderName, subFolders, fileNames in os.walk(folder):
        folderSize = os.path.getsize(folderName)

        for fileName in fileNames:
            fileLocation = os.path.join(folderName, fileName)
            fileSize = os.path.getsize(fileLocation)
            folderSize += fileSize

            if fileSize > sizeLimit:
                print(fileLocation+' is a YUGE file!!!')

        if folderSize > sizeLimit:
            print(folderName+' is a YUGE folder!!!')

massiveFileSearch(FOLDER, 500)
