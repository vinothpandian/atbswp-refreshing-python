#! python

import os, re

FOLDER = './P2C83-RegexSearch'

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

def regexSearch(path, regex):
    os.chdir(path)

    for file in os.listdir():
        if os.path.isfile(file):
            searchFile = open(file)
            text = searchFile.read()
            found = re.findall(regex, text)
            for text in found:
                print(text)
            searchFile.close()

regexSearch(FOLDER, r'[\d]+')
