import json
import os
import time
from fbchat_v2 import Client

# 1. Config aur Appstate Load Karna
with open('src/config.json', 'r') as f:
    config = json.load(f)

# appstate.json file ko read karna (Jo aapne abhi banayi hai)
try:
    with open('appstate.json', 'r') as f:
        appstate = json.load(f)
except FileNotFoundError:
    print("Error: appstate.json file nahi mili!")
    exit()

class YuviBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # Bot sirf owner ki baat sunega ya sabki, yahan logic aayega
        if author_id == self.uid:
            return

        # Basic Help Command Check
        if message_object.text == f"{config['prefix']}info":
            # Yahan wahi Sukuna photo aur admin card aayega
            print(f"Command received from: {author_id}")

# 2. Bot ko Login Karwana
client = YuviBot("", "", session_cookies=appstate)

print(f"Bot Name: {config['botName']}")
print(f"Owner ID: {config['ownerID'][0]}")
print("Status: Yuvi Bot is Online! 🚀")

client.listen()
