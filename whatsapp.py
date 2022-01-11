import time
import datetime as dt
import json
import os
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class WhatsAppElements:
    search = (By.CSS_SELECTOR, "#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text")


class WhatsApp:
    browser =  None
    timeout = 10  # The timeout is set for about ten seconds
    def __init__(self, wait, screenshot=None, session=None):
        exe_path = r"C:\Users\Quintine\Downloads\chromedriver_win32\chromedriver.exe"
        self.browser = webdriver.Chrome(executable_path=exe_path)
        self.browser.get("https://web.whatsapp.com/") #to open the WhatsApp web
        # you need to scan the QR code in here (to eliminate this step, I will publish another blog
        WebDriverWait(self.browser,wait).until(
        EC.presence_of_element_located(WhatsAppElements.search)) #wait till search element appears

    def unread_usernames(self, scrolls=20):
        initial = 10
        usernames = []
        for i in range(0, scrolls):
            self.browser.execute_script("document.getElementById('pane-side').scrollTop={}".format(initial))
            soup = BeautifulSoup(self.browser.page_source, "html.parser")
            for i in soup.find_all("div", class_="_3uIPm WYyr1"):
                if i.find("div", class_="_3m_Xw"):
                    username = i.find("div", class_="zoWT4").text
                    print(username)
                    usernames.append(username)
            initial += 10
        # Remove duplicates
        usernames = list(set(usernames))
        return usernames

    def get_last_message_for(self, name):
        messages = list()
        search = self.browser.find_element(*WhatsAppElements.search)
        search.send_keys(name + Keys.ENTER)
        time.sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        for i in soup.find_all("div", class_="message-in"):
            message = i.find("span", class_="selectable-text")
            if message:
                message2 = message.find("span")
                if message2:
                    messages.append(message2.text)
        messages = list(filter(None, messages))
        return messages



