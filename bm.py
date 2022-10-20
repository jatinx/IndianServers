#!/usr/bin/env python

import requests

TOKEN = '' # Paste the token between two quotes

HEADERS = {"Authorization" : "Bearer " + TOKEN}
URL = 'https://api.battlemetrics.com/servers?filter[countries]=IN&page[size]=100'

if __name__ == "__main__":
    if len(TOKEN) == 0:
        print('Token seems to be empty, please generate a token and paste it in TOKEN variable')
        exit()
    games = list()
    games.append('valorant') # Valorant is known to have Indian servers
    while True:
        try:
            response = requests.get(URL, headers=HEADERS)
        except Exception as e:
            print("Failed to get with: ", e)
            break
        j = response.json()
        try:
            URL = j['links']['next']
        except Exception as e:
            break # break the loop since there is no next tag in json
        for i in j['data']:
            games.append(i['relationships']['game']['data']['id'])
    
    print ('List of games with Indian Server:')
    for i in sorted(set(games)):
        print('  ', i)
