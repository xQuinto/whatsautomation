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

    if user_input.lower() == "weer":
        location, message = get_day_phrase_and_weather()
        int_hour, int_minutes = time_to_send()

        send_more = input("Do you want to repeat this message? Type 1 for yes and 2 for no")
        if send_more == "1":
            repeat = int(input("How many times do you wish to send this message?"))
            interval = int(input("How many minutes you want to have between those messages?"))

            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()

            i = 1
            while i < repeat:
                int_minutes = int_minutes + interval
                while int_minutes > 59:
                    int_minutes = int_minutes - 60
                    int_hour = int_hour + 1

                message = weather_message(interval, location)
                pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
                make_screenshot()
                i = i + 1
        elif send_more == "2":
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()
        else:
            print("I did not understand your answer. I'll send the message just once")
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()

    if user_input.lower() == "weer en nieuws":
        message, location, reciever = news.get_weather_and_news()
        int_hour, int_minutes = time_to_send()

        send_more = input("Do you want to repeat this message? Type 1 for yes and 2 for no")
        if send_more == "1":
            repeat = int(input("How many times do you wish to send this message?"))
            interval = int(input("How many minutes you want to have between those messages?"))

            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()
            i = 1
            while i < repeat:
                int_minutes = int_minutes + interval
                while int_minutes > 59:
                    int_minutes = int_minutes - 60
                    int_hour = int_hour + 1

                message = news.get_weather_and_news_repeat(location, reciever)
                pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
                make_screenshot()
                i = i + 1
        elif send_more == "2":
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()
        else:
            print("I did not understand your answer. I'll send the message just once")
            pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
            make_screenshot()

    # Nog meerdere keren versturen ondersteunen (dan ook zonder day phrase functie)
    if user_input.lower() == "nieuws":
        message = news.get_latest_news_message()
        int_hour, int_minutes = time_to_send()
        pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
        make_screenshot()

    if user_input.lower() == "lol":
        message = lol.get_all_ranked_info()
        int_hour, int_minutes = time_to_send()
        pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
        make_screenshot()
    # int_hour, int_minutes = time_to_send()
    # send_more = input("Do you want to repeat this message? Type 1 for yes and 2 for no")
    #
    # if send_more == "1":
    #     repeat = int(input("How many times do you wish to send this message?"))
    #     interval = int(input("How many minutes you want to have between those messages?"))
    #     pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
    #     make_screenshot()
    #
    #     i = 1
    #     while i < repeat:
    #         int_minutes = int_minutes + interval
    #         while int_minutes > 59:
    #             int_minutes = int_minutes - 60
    #             int_hour = int_hour + 1
    #
    #         if nieuws:
    #             message = news.send_latest_news()
    #
    #         pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
    #         make_screenshot()
    #         i = 1 + i
    # elif send_more == "2":
    #     pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
    #     make_screenshot()
    # else:
    #     print("I did not understand your answer. I'll send the message just once")
    #     pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)
    #     make_screenshot()


def read_message():
    # Creating the driver (browser)
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Login
    #       and uncheck the remember check box
    #       (Get your phone ready to read the QR code)
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(30)

    # 1. Get all opened chats
    #       opened chats are the one chats or conversations
    #       you already have in your whatsapp.
    #       IT WONT work if you are looking for a contact
    #       you have never started a conversation.
    pane_page = PanePage(driver)

    # get all chats
    opened_chats = pane_page.opened_chats

    # iterating over them
    for oc in opened_chats:
        print(oc.name)  # contact name (as appears on your whatsapp)
        print(oc.icon)  # the url of the image
        print(oc.last_message)
        print(oc.last_message_time)  # datetime object
        print(oc.has_notifications())  # are there unread messages?
        print(oc.notifications)  # returns a integer with the qty of new messages, if there are.

    # 2. Go into the chat
    #       just click on one to open the chat page
    #       (where the conversation is happening)
    first_chat = opened_chats[0]
    first_chat.click()

    # 3. Read the last 10 messages from your contact
    chat_page = ChatPage(driver)
    msgs = chat_page.messages.newest(10, filterby='contact')

    for msg in msgs:
        print(msg.contact)  # name (all should be the same)
        print(msg.date)
        print(msg.text)
        print(msg.status)

    # 4. Reply to the most recent message
    msg = msgs[0]  # get the first of the messages query done in previous step
    msg = chat_page.messages.newest(filterby='contact')
    # Be careful as library can only now reply to text message
    # Replying to a msg type (video, image, giff, etc) is not implemented yet.
    msg.reply("This a reply to a specific text msg.")

    # Logout
    header_page = HeaderPage(driver)
    header_page.logout()

    # Close the browser
    driver.quit()


if __name__ == '__main__':
    # print("hoi")
    #read_message()
    send_message()
    #get_weather()
    #   get_league_puuid()
    #lol.get_tft_info_with_id()
    #   get_encrypted_summoner_id()
    #   get_league_id()

    # #Hieronder ook functie van maken
    # lol.get_all_ranked_info()
    # phone_number = input("Enter phone number to which you wanna send a text:")
    # message = lol.get_all_ranked_info()
    # print("Now lets talk about the time you want it to send. I'll ask you the hours(24) and minutes apart.")
    # hour = input("hour:")
    # minutes = input("minutes:")
    # int_hour = int(hour)
    # int_minutes = int(minutes)
    # while int_minutes > 59:
    #     int_minutes = int_minutes - 60
    #     int_hour = int_hour + 1
    # pywhatkit.sendwhatmsg(phone_number, message, int_hour, int_minutes)

    # news.send_latest_news()

