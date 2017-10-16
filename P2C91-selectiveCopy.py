#! python

import os, shutil

FOLDER = 'P2C83-RegexSearch'

def selectiveCopy(folder, newFolder, extension):

    if not os.path.exists(newFolder):
        os.mkdir(newFolder)

    for folderName, subFolders, fileNames in os.walk(FOLDER):

        for fileName in fileNames:
            if fileName.endswith('.'+extension):
                oldLocation = os.path.join(folderName, fileName)
                newLocation = os.path.join(newFolder, fileName)
                shutil.copy(oldLocation, newLocation)
                print('File: %s is copied to %s' %(oldLocation, newLocation))

selectiveCopy(FOLDER, 'P2C91-CopyHere', 'py')
