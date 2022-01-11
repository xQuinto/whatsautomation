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


def get_tft_info():
    API_KEY = "RGAPI-5f5aea2a-d9cf-4bc7-960a-ec2ea7f49a10"

    summoner_id = get_league_id()
    league_url = f"https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    tier = league_data[0]['tier']
    rank = league_data[0]['rank']
    pprint(league_data)
    queue_type = league_data[0]['queueType']
    summoner_name = league_data[0]['summonerName']

    print(f"Hello {summoner_name}, in {queue_type} you are {tier} {rank}")

#Ook functie voor solo maken
def get_all_ranked_info():
    API_KEY = "RGAPI-5f5aea2a-d9cf-4bc7-960a-ec2ea7f49a10"

    summoner_id = get_league_id()
    league_url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    pprint(league_data)

    message = f"Hi, I don't have any ranked info for you :("
# zo kan ik ook checken op len(data) == 1 bv etc en zo meer weergeven
    if len(league_data):
        queue_type = league_data[0]['queueType']
        if queue_type == 'RANKED_FLEX_SR':
            message = get_ranked_flex(league_data, 0)
            queue_type = league_data[1]['queueType']
        elif queue_type == 'RANKED_TFT_PAIRS':
            message = get_ranked_tft_pairs(league_data, 0)

    print(message)
    return message


# if queuetype = blabla dan doe dit, zeg maar een bool/false/true statement hierboven per queue type

def get_ranked_tft_pairs(league_data, x):
    summoner_name = league_data[x]['summonerName']
    wins = league_data[x]['wins']
    losses = league_data[x]['losses']
    queue_type = league_data[x]['queueType']

    message_rank = f"Hello {summoner_name}, in {queue_type} you have {wins} wins and {losses} losses.\n"
    message_other = "I couldn't find any Summoners Rift ranked data for you. Please first play all your placements"
    message = message_rank + message_other

    return message


def get_ranked_flex(league_data, x):
    summoner_name = league_data[x]['summonerName']
    wins = league_data[x]['wins']
    losses = league_data[x]['losses']
    tier = league_data[x]['tier']
    rank = league_data[x]['rank']
    queue_type = league_data[x]['queueType']

    message_rank = f"Hello {summoner_name}, in {queue_type} you are {tier} {rank}.\n"
    message_games = f"You have {wins} wins and {losses} losses."
    message = message_rank + message_games

    return message


def get_league_puuid():
    API_KEY = "RGAPI-5f5aea2a-d9cf-4bc7-960a-ec2ea7f49a10"

    summoner_name = input("What is the summoner name you want to look up? ")

    league_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    return league_data['puuid']


#dit is de encrypted summoner id
def get_league_id():
    API_KEY = "RGAPI-5f5aea2a-d9cf-4bc7-960a-ec2ea7f49a10"

    summoner_name = input("What is the summoner name you want to look up? ")

    league_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key="
    final_url = league_url + API_KEY

    league_data = requests.get(final_url).json()
    pprint(league_data)
    return league_data['id']
