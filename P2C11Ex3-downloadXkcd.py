#! python

import requests, bs4, os, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
url = 'http://xkcd.com/1524/'
os.makedirs("xkcd", exist_ok=True)

while not url.endswith('#'):
    print("Downloading page %s...." %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    comic = soup.select('#comic img')
    if comic == []:
        print("Comic not found...")
    else:
        comicUrl = comic[0].get("src")
        # logging.debug(comicUrl)
        print("Downloading comic %s..." %comicUrl)
        imgRes = requests.get('http:%s' %comicUrl)
        imgRes.raise_for_status()

        comicFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), 'wb')
        for chunk in imgRes.iter_content(100000):
            comicFile.write(chunk)

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print('Done.')
