#! python3

import os, re

FOLDER = './P2C82-MadLibs'
FILE = 'madlib.txt'

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

os.chdir(FOLDER)

keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

madFile = open(FILE,'r')
correctedMadFile = open('corrected-'+FILE,'w')

text = madFile.readlines()
replacedText = ''

keywordRegEx = re.compile(r'[A-Z]+')

for line in text:
    line = str(line)
    found = list(re.findall(keywordRegEx, line))

    for keyword in found:
        if keyword in keywords:
            print('Enter an ' + keyword.lower())
            word = input()
            line = line.replace(keyword, word)

    correctedMadFile.write(line)
    replacedText += line

madFile.close()
correctedMadFile.close()

print('\nHere is your new text:')
print(replacedText)
