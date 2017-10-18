#! python

import requests, bs4, os, logging, threading

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
os.makedirs("multiThread_Xkcd", exist_ok=True)


def xkcdDownloader(start_comic, end_comic):
    url = 'http://xkcd.com/'

    for comic_num in range(start_comic, end_comic):
        # logging.debug(url+str(comic_num))
        res = requests.get(url + str(comic_num))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        comic = soup.select('#comic img')
        if comic == []:
            print("Comic not found...")
        else:
            comicUrl = comic[0].get("src")
            # logging.debug(comicUrl)
            print("Downloading comic %s..." % os.path.basename(comicUrl))
            try:
                imgRes = requests.get('http:%s' % comicUrl)
                imgRes.raise_for_status()
            except requests.RequestException:
                print("Couldn't find comic...")

            comicFile = open(os.path.join("multiThread_Xkcd", os.path.basename(comicUrl)), 'wb')
            for chunk in imgRes.iter_content(100000):
                comicFile.write(chunk)
            comicFile.close()


downloadThreads = []

for i in range(1, 1900, 100):
    downloadThread = threading.Thread(target=xkcdDownloader, args=[i, i + 99])
    downloadThreads.append(downloadThread)
    downloadThread.start()

for thread in downloadThreads:
    thread.join()

print("Done")
