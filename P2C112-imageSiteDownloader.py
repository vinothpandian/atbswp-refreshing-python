#! python

import sys, os, logging
import requests, bs4
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

if len(sys.argv) > 1:
    keywords = '+'.join(sys.argv[1:])
    keywordsList = ' '.join(sys.argv[1:])
else:
    print("Run the program as P2C112-imageSiteDownloader.py [Keywords]")
    sys.exit()

FOLDER_NAME = "./P2C112-imageSiteDownload"

os.makedirs(FOLDER_NAME, exist_ok=True)
os.chdir(FOLDER_NAME)

URL = "https://imgur.com/search?q="+keywords

response = requests.get(URL)
response.raise_for_status()

print("Searching for \"%s\" in imgur........." % keywordsList)

soup = bs4.BeautifulSoup(response.text, "html.parser")
images = soup.select(".home-gallery .cards img")
# logging.debug("Content is \n %s" % images)

imgCount = 0

for image in images:
    imgURL = "http:"+image.get('src')

    imgRes = requests.get(imgURL)
    imgRes.raise_for_status()
    imgCount += 1
    print("Downloading %s image %d..." % (keywordsList, imgCount))
    imgFile = open(os.path.join(os.getcwd(), '_'.join([str(imgCount),keywordsList,os.path.basename(imgURL)])), 'wb')
    for chunk in imgRes.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()
    imgRes.close()

response.close()

