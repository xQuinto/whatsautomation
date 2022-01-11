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
from utils import *


def weather_message(interval, location):
    weather_object = get_weather_with_location(location)
    feels_like = str(weather_object['main']['feels_like'])
    location = weather_object['name']
    now = datetime.datetime.now()
    dag_teksts = dag_tekst(now)
    time_stamp = str(now.hour) + ":" + str(now.minute + interval)
    message = dag_teksts + "it feels like " + feels_like + " degrees in " + location + " at " + time_stamp
    return message


def get_day_phrase_and_weather():
    weather = get_weather()
    feels_like = str(weather['main']['feels_like'])
    location = weather['name']
    now = datetime.datetime.now()
    day_phrase = dag_tekst(now)
    #Dit nog aanpassen naar verder gedetailleerde weers(voorspelling/statistieken)
    message = day_phrase + "it feels like " + feels_like + " degrees celcius in " + location
    return location, message


def get_weather_with_location(location):
    API_KEY = "534f23b68fb8dc08545c7c524833ac7a"

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid="
    final_url = weather_url + API_KEY

    weather_data = requests.get(final_url).json()
    return weather_data


def get_weather():
    API_KEY = "534f23b68fb8dc08545c7c524833ac7a"

    location = input("Enter your desired location: ")

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid="
    final_url = weather_url + API_KEY

    weather_data = requests.get(final_url).json()
    return weather_data





