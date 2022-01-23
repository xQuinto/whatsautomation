import pywhatkit
import datetime
import time
import requests

from selenium import webdriver
from pprint import pprint

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage
from simon.pages import BasePage

import league_of_legends as lol
import news as news
from weather import *
from utils import *


def send_message():
    phone_number = input("Enter phone number to which you wanna send a text:")
    user_input = input("Enter your message:")

    # van alle ifs een case ofzo maken
    if user_input.lower() == "weer":
        location, message = get_day_phrase_and_weather()
        int_hour, int_minutes = time_to_send()

        send_more = input("Do you want to repeat this message? Type 1 for yes and 2 for no")
        if send_more == "1":
            repeat = int(input("How many times do you wish to send this message?"))
            interval = int(input("How many minutes you want to have between those messages?"))

            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()

            i = 1
            while i < repeat:
                int_minutes = int_minutes + interval
                while int_minutes > 59:
                    int_minutes = int_minutes - 60
                    int_hour = int_hour + 1

                message = weather_message(interval, location)
                pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
                ##make_screenshot()
                i = i + 1
        elif send_more == "2":
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()
        else:
            print("I did not understand your answer. I'll send the message just once")
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()

    if user_input.lower() == "weer en nieuws":
        message, location, reciever = news.get_weather_and_news()
        int_hour, int_minutes = time_to_send()

        send_more = input("Do you want to repeat this message? Type 1 for yes and 2 for no")
        if send_more == "1":
            repeat = int(input("How many times do you wish to send this message?"))
            interval = int(input("How many minutes you want to have between those messages?"))

            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()
            i = 1
            while i < repeat:
                int_minutes = int_minutes + interval
                while int_minutes > 59:
                    int_minutes = int_minutes - 60
                    int_hour = int_hour + 1

                message = news.get_weather_and_news_repeat(location, reciever)
                pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
                ##make_screenshot()
                i = i + 1
        elif send_more == "2":
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()
        else:
            print("I did not understand your answer. I'll send the message just once")
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            ##make_screenshot()

    # Nog meerdere keren versturen ondersteunen (dan ook zonder day phrase functie)
    if user_input.lower() == "nieuws":
        message = news.get_latest_news_message()
        int_hour, int_minutes = time_to_send()
        pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
        ##make_screenshot()

    if user_input.lower() == "lol":
        message = lol.get_all_ranked_info()
        int_hour, int_minutes = time_to_send()
        pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
        ##make_screenshot()


if __name__ == '__main__':
    # print("hoi")

    #read_message()
    send_message()
    #get_weather()

    # news.send_latest_news()

