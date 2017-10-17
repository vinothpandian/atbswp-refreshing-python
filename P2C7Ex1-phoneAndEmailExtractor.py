#! python

import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
    )''', re.VERBOSE)

text = pyperclip.paste()

phoneNumbers = phoneRegex.findall(text)
emailIDs = emailRegex.findall(text)

extracted = []

for group in phoneRegex.findall(text):
    extracted.append(group[0].replace('.','-'))

for group in emailRegex.findall(text):
    extracted.append(group[0])

if len(extracted) > 0:
    text = '\n'.join(extracted)
    pyperclip.copy(text)
    print("Copied to clipboard:")
    print(text)
else:
    print("No phone numbers or email addresses found")
