#!python

import pyperclip, shelve, sys, os

MCB_FOLDER = './P2C8Ex2-MultiClipboard'

if not os.path.exists(MCB_FOLDER):
    os.mkdir(MCB_FOLDER)

os.chdir(MCB_FOLDER)

mcbShelve = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelve[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])

mcbShelve.close()
