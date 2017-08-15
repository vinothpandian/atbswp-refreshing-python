#!python3

import requests, bs4
import webbrowser, sys

print("Googling......................")
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElem = soup.select('.r a')

numRes = min(5, len(linkElem))

for result in range(numRes):
    webbrowser.open('http://google.com' + linkElem[result].get('href'))
