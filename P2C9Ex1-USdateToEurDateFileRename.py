#!python3

import shutil, os, re

datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

PATH = './P2C83-RegexSearch'

for fileName in os.listdir(PATH):

    date = re.search(datePattern, fileName)

    if not os.path.isfile(os.path.join(PATH,fileName)) or date == None:
        continue

    beforePart = date.group(1)
    monthPart = date.group(2)
    dayPart = date.group(4)
    yearPart = date.group(6)
    afterPart = date.group(8)

    eurDate = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath(PATH)
    usDate = os.path.join(absWorkingDir, fileName)
    eurDate = os.path.join(absWorkingDir, eurDate)

    print('Renaming "%s" to "%s"...' % (usDate, eurDate))
    #shutil.move(usDate, eurDate)
