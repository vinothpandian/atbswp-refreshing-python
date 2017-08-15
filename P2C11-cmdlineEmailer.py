#! python3

import requests, bs4, sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

USERNAME = "" # Enter your username of yandex
PASSWORD = "" # Enter your Password of yandex

if len(sys.argv) > 3:
    email = sys.argv[1]
    message = ' '.join(sys.argv[2:])
    subject = sys.argv[2]
    print(" Sending the message: %s\nTo: %s................." %(message, email))
else:
    print("Please run the program with email and message P2C11-cmdlineEmailer.py [email] [message]")
    sys.exit()

browser = webdriver.Firefox()
browser.get('https://mail.yandex.com/')
actions = ActionChains(browser)
timeout= 5

usernameElem = browser.find_element_by_name("login")
usernameElem.send_keys(USERNAME)

pwdElem = browser.find_element_by_name("passwd")
pwdElem.send_keys(PASSWORD, Keys.ENTER)

try:
    myElem = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'mail-ComposeButton')))
    print( "Page is ready!")
except TimeoutException:
    print( "Loading took too much time!")

headElem = browser.find_element_by_tag_name("html")
headElem.send_keys("w")

try:
    myElem = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'mail-Compose-Message js-compose-message')))
    print( "Page is ready!")
except TimeoutException:
    print( "Loading took too much time!")

actions.send_keys(email, Keys.TAB, subject, Keys.TAB, message)
actions.key_down( Keys.CONTROL).send_keys(Keys.ENTER)
actions.perform()
