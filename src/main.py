import json
import time
from fbchat_v2 import Client
# Aapki lock wali file ko import kar rahe hain
from commands.admin_locks import AdminLocks 

# 1. Config aur Appstate Load Karna
with open('src/config.json', 'r') as f:
    config = json.load(f)

try:
    with open('appstate.json', 'r') as f:
        appstate = json.load(f)
except FileNotFoundError:
    print("Error: appstate.json nahi mili! Check karein.")
    exit()

class YuviBot(Client):
    def onListen(self):
        # AdminLocks class ko bot ke andar active karna
        self.locks = AdminLocks(self)
        print("✅ Yuvi's Anti-Admin System is Ready and Waiting!")

    # --- YE EVENTS LOCK KO CHALAYENGE ---

    # 1. Group Name badalne par check karega
    def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
        self.locks.handle_title_change(author_id, thread_id, thread_type)

    # 2. Nickname badalne par check karega
    def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
        self.locks.handle_nick_change(author_id, changed_for, thread_id, thread_type)

    # 3. Aapki Commands Sunne ke liye
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        msg = message_object.text.lower()
        
        # Sirf Aap (Owner) hi lock ON/OFF kar sakte ho
        if author_id == config['ownerID'][0]:
            # Ye line locks file mein command bhejegi
            self.locks.process_command(msg, thread_id, thread_type)

# 2. Bot Login
client = YuviBot("", "", session_cookies=appstate)
client.listen()
