#! python

import zipfile, os

def backupToZip(folder):

    folder = os.path.abspath(folder)
    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for folderName, subFolders, fileNames in os.walk(folder):
        print('Adding files in %s...' % (folderName))
        backupZip.write(folderName)

        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue

            backupZip.write(os.path.join(folderName, fileName))

    backupZip.close()
    print('Done.')

backupToZip('./P2C8Ex2-MadLibs')
