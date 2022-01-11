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

from main import *


def get_weather_and_news():
    #location, weer = get_day_phrase_and_weather()
    weather = get_weather()
    feels_like = str(weather['main']['feels_like'])
    location = weather['name']

    news_data = get_news()
    receiver = input("wat is de ontvangersnaam?")
    article_description_0 = news_data['articles'][0]['description']
    article_url_0 = news_data['articles'][0]['url']
    intro = f"Hallo {receiver}, het voelt momenteel {feels_like} graden in {location}.\n" \
            f"Dit zijn de top 3 nieuwsartikelen op dit moment: \n"
    message_0 = article_description_0 + "\n" + article_url_0 + "\n\n"

    article_description_2 = news_data['articles'][2]['description']
    article_url_2 = news_data['articles'][2]['url']
    message_2 = article_description_2 + "\n" + article_url_2 + "\n\n "
    message_0 = message_0 + message_2

    article_description_3 = news_data['articles'][3]['description']
    article_url_3 = news_data['articles'][3]['url']
    message_3 = article_description_3 + "\n" + article_url_3
    message_0 = intro + message_0 + message_3

    return message_0, location, receiver


def get_weather_and_news_repeat(location, receiver):
    #location, weather = get_day_phrase_and_weather()
    weather = get_weather_with_location(location)
    feels_like = str(weather['main']['feels_like'])
    location = weather['name']

    news_data = get_news()
    article_description_0 = news_data['articles'][0]['description']
    article_url_0 = news_data['articles'][0]['url']
    intro = f"Hallo {receiver}, het voelt momenteel {feels_like} graden in {location}.\n" \
            f"Dit zijn de top 3 nieuwsartikelen op dit moment: \n"
    message_0 = article_description_0 + "\n" + article_url_0 + "\n\n"

    article_description_2 = news_data['articles'][2]['description']
    article_url_2 = news_data['articles'][2]['url']
    message_2 = article_description_2 + "\n" + article_url_2 + "\n\n "
    message_0 = message_0 + message_2

    article_description_3 = news_data['articles'][3]['description']
    article_url_3 = news_data['articles'][3]['url']
    message_3 = article_description_3 + "\n" + article_url_3
    message_0 = intro + message_0 + message_3

    return message_0


def get_latest_news_message():
    news_data = get_news()
    receiver = input("wat is de ontvangersnaam?")
    article_description_0 = news_data['articles'][0]['description']
    article_url_0 = news_data['articles'][0]['url']
    intro = f"Hallo {receiver}, dit zijn de top 3 nieuwsartikelen op dit moment: \n"
    message_0 = article_description_0 + "\n" + article_url_0 + "\n\n"

    article_description_2 = news_data['articles'][2]['description']
    article_url_2 = news_data['articles'][2]['url']
    message_2 = article_description_2 + "\n" + article_url_2 + "\n\n "
    message_0 = message_0 + message_2
    # article_description_2 = news_data['articles'][2]['description']
    # article_url_2 = news_data['articles'][2]['url']
    # message_2 = article_description_2 + "\n" + article_url_2

    article_description_3 = news_data['articles'][3]['description']
    article_url_3 = news_data['articles'][3]['url']
    message_3 = article_description_3 + "\n" + article_url_3
    message_0 = intro + message_0 + message_3

    return message_0


def get_news():
    API_KEY = "40bf75b4708a446da2d6237c1e9deb30"
    news_url = "https://newsapi.org/v2/top-headlines?country=nl&apiKey="
    final_url = news_url + API_KEY
    news_data = requests.get(final_url).json()
    return news_data
