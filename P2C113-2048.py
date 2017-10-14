#! python3

import sys, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

browser = webdriver.Firefox()
URL = 'https://gabrielecirulli.github.io/2048/'

browser.get(URL)

siteBody = browser.find_element_by_tag_name('body')

while True:
    siteBody.send_keys(Keys.UP)
    siteBody.send_keys(Keys.RIGHT)
    siteBody.send_keys(Keys.DOWN)
    siteBody.send_keys(Keys.LEFT)

    try:
        browser.find_element_by_class_name('game-over')
        scoreContainer = browser.find_element_by_class_name('score-container')
        logging.debug('Container is %s' % scoreContainer.get_attribute("outerHTML"))
        scoreSoup = bs4.BeautifulSoup(scoreContainer.get_attribute("outerHTML"), "html.parser")
        logging.debug('Soup is %s' %scoreSoup)
        score = scoreSoup.find(text=True)
        print("Your score is %s" % score)
        break
    except:
        continue
