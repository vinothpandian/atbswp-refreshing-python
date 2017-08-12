#!python3

import re

def strip(text, replace='\s'):
    startRegEx = re.compile(r'^'+ replace +'*')
    endRegEx = re.compile(replace+'*$')
    text = re.sub(startRegEx, '', text)
    text = re.sub(endRegEx, '', text)
    print(text)

strip("Hello WorldHe", 'He')
strip("  Hello World              ")
