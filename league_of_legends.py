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


def get_tft_info(summoner_id):
    API_KEY = "RGAPI-5dc31456-34ab-4a6d-8a44-87c35547ef13"

    #summoner_id = get_league_id()
    #get_league_id_summoner_name()
    league_url = f"https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    #pprint(league_data)
    tier = league_data[0]['tier']
    rank = league_data[0]['rank']
    #pprint(league_data)
    queue_type = league_data[0]['queueType']
    summoner_name = league_data[0]['summonerName']

    #print(f"Hello {summoner_name}, in {queue_type} you are {tier} {rank}")
    message = f"In {queue_type} you are {tier} {rank}"
    return message

#Ook functie voor solo maken
def get_all_ranked_info():
    API_KEY = "RGAPI-5dc31456-34ab-4a6d-8a44-87c35547ef13"

    summoner_id = get_league_id()
    league_url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    #print(len(league_data))
    pprint(league_data)

    message = f"Hi, I don't have any ranked info for you :("

    if len(league_data) == 1:
        queue_type = league_data[0]['queueType']
        if queue_type == 'RANKED_FLEX_SR':
            message = get_ranked_flex(league_data, 0)
        elif queue_type == 'RANKED_TFT_PAIRS':
            message = get_ranked_tft_pairs(league_data, 0)
        elif queue_type == 'RANKED_SOLO_5x5':
            message = get_ranked_solo(league_data, 0)

    elif len(league_data) == 2:
        queue_type_0 = league_data[0]['queueType']
        queue_type_1 = league_data[1]['queueType']

        if queue_type_0 == 'RANKED_FLEX_SR':
            message_0 = get_ranked_flex(league_data, 0)
        elif queue_type_0 == 'RANKED_TFT_PAIRS':
            message_0 = get_ranked_tft_pairs(league_data, 0)
        elif queue_type_0 == 'RANKED_SOLO_5x5':
            message_0 = get_ranked_solo(league_data, 0)

        if queue_type_1 == 'RANKED_FLEX_SR':
            message_1 = get_ranked_flex(league_data, 1)
        elif queue_type_1 == 'RANKED_TFT_PAIRS':
            message_1 = get_ranked_tft_pairs(league_data, 1)
        elif queue_type_1 == 'RANKED_SOLO_5x5':
            message_1 = get_ranked_solo(league_data, 1)

        message = message_0 + "\n" + message_1

    elif len(league_data) == 3:
        queue_type_0 = league_data[0]['queueType']
        queue_type_1 = league_data[1]['queueType']
        queue_type_2 = league_data[2]['queueType']

        if queue_type_0 == 'RANKED_FLEX_SR':
            message_0 = get_ranked_flex(league_data, 0)
        elif queue_type_0 == 'RANKED_TFT_PAIRS':
            message_0 = get_ranked_tft_pairs(league_data, 0)
        elif queue_type_0 == 'RANKED_SOLO_5x5':
            message_0 = get_ranked_solo(league_data, 0)

        if queue_type_1 == 'RANKED_FLEX_SR':
            message_1 = get_ranked_flex(league_data, 1)
        elif queue_type_1 == 'RANKED_TFT_PAIRS':
            message_1 = get_ranked_tft_pairs(league_data, 1)
        elif queue_type_1 == 'RANKED_SOLO_5x5':
            message_1 = get_ranked_solo(league_data, 1)

        if queue_type_2 == 'RANKED_FLEX_SR':
            message_2 = get_ranked_flex(league_data, 2)
        elif queue_type_2 == 'RANKED_TFT_PAIRS':
            message_2 = get_ranked_tft_pairs(league_data, 2)
        elif queue_type_2 == 'RANKED_SOLO_5x5':
            message_2 = get_ranked_solo(league_data, 2)

        message = message_0 + "\n" + message_1 + "\n" + message_2

    tft_solo = get_tft_info(summoner_id)

    if (tft_solo):
        message = message + tft_solo

    #print(message)
    return message


# ranked_tft_pairs
def get_ranked_tft_pairs(league_data, x):
    summoner_name = league_data[x]['summonerName']
    wins = league_data[x]['wins']
    losses = league_data[x]['losses']
    queue_type = league_data[x]['queueType']
    # hot streak kan ook nog vermeld worden

    message_rank = f"Hello {summoner_name}, in {queue_type} you have {wins} wins and {losses} losses.\n"
    #message_other = "I couldn't find any Summoners Rift ranked data for you. Please first play all your placements"
    message = message_rank #+ message_other

    return message


# ranked_flex_sr
def get_ranked_flex(league_data, x):
    summoner_name = league_data[x]['summonerName']
    wins = league_data[x]['wins']
    losses = league_data[x]['losses']
    tier = league_data[x]['tier']
    rank = league_data[x]['rank']
    queue_type = league_data[x]['queueType']
    #hot streak kan ook nog vermeld worden

    message_rank = f"Hello {summoner_name}, in {queue_type} you are {tier} {rank}.\n"
    message_games = f"You have {wins} wins and {losses} losses."
    message = message_rank + message_games

    return message


# ranked_solo_5x5
def get_ranked_solo(league_data, x):
    summoner_name = league_data[x]['summonerName']
    wins = league_data[x]['wins']
    losses = league_data[x]['losses']
    tier = league_data[x]['tier']
    rank = league_data[x]['rank']
    queue_type = league_data[x]['queueType']
    # hot streak kan ook nog vermeld worden

    message_rank = f"Hello {summoner_name}, in {queue_type} you are {tier} {rank}.\n"
    message_games = f"You have {wins} wins and {losses} losses."
    message = message_rank + message_games

    return message


def get_league_puuid():
    API_KEY = "RGAPI-5dc31456-34ab-4a6d-8a44-87c35547ef13"

    summoner_name = input("What is the summoner name you want to look up? ")

    league_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    return league_data['puuid']


#dit is de encrypted summoner id
def get_league_id():
    API_KEY = "RGAPI-5dc31456-34ab-4a6d-8a44-87c35547ef13"

    summoner_name = input("What is the summoner name you want to look up? ")

    league_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    pprint(league_data)
    return league_data['id']


def get_league_id_summoner_name(summoner_name):
    API_KEY = "RGAPI-5dc31456-34ab-4a6d-8a44-87c35547ef13"
    #summoner_name = input("What is the summoner name you want to look up? ")

    league_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    pprint(league_data)
    return league_data['id']
