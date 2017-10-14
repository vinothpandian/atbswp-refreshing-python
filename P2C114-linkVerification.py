#! python

import requests, bs4

URL = "http://vinothpandian.me"

response = requests.get(URL)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")
links = soup.select("a")

isAnyLinkDeadFlag = False

for link in links:
    hrefURL = link.get('href')

    try:
        linkRes = requests.get(hrefURL)
    except:
        if (linkRes.status_code == 404):
            print("Dead link : %s", hrefURL)
        linkRes.close()

if not isAnyLinkDeadFlag:
    print("No dead link in the given URL")

response.close()