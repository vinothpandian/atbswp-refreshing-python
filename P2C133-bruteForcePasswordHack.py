#! python

import os, PyPDF2
import random

FOLDER_NAME = "P2C13"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

dictFile = open("dictionary.txt")
dict = dictFile.readlines()

pdfFile = open("Page_1_encrypted.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)


def sampling(dict, value):
    random_sample = []
    for i in range(value):
        list_length = len(dict)
        if list_length != 0:
            random_sample.append(dict.pop(random.randrange(list_length)))
    return random_sample


isPasswordFound = False

while not isPasswordFound:
    sample = sampling(dict, 1000)

    if not sample:
        print("Your password was not found in the dictionary")
        break

    for word in sample:
        if pdfReader.decrypt(word.strip()):
            print("The password is %s" % word.strip())
            isPasswordFound = True
            break
        elif pdfReader.decrypt(word.lower().strip()):
            print("The password is %s" % word.lower().strip())
            isPasswordFound = True
            break
