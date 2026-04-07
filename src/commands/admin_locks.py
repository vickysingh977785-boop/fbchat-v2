import time

# Settings
OWNER_ID = "61567276533610"
SUKUNA_IMG = "https://i.ibb.co/WvHj4HZP/IMG-20260404-191841.png"

class AdminLocks:
    def __init__(self, client):
        self.client = client
        self.namelock_active = False # Shuru me OFF rahega
        self.nicklock_active = False # Shuru me OFF rahega
        self.locked_title = ""

    # --- COMMANDS CONTROLLER ---
    def process_command(self, msg, thread_id, thread_type):
        # 1. Name Lock Commands
        if msg == "+namelock on":
            self.namelock_active = True
            # Jo abhi naam hai, wahi lock ho jayega
            self.locked_title = self.client.fetchThreadInfo(thread_id)[thread_id].name
            self.client.send(f"🔒 Name Lock Active! (Target: {self.locked_title})", thread_id, thread_type)
        
        elif msg == "+namelock off":
            self.namelock_active = False
            self.client.send("🔓 Name Lock Disabled!", thread_id, thread_type)

        # 2. Nickname Lock Commands
        if msg == "+nicklock on":
            self.nicklock_active = True
            self.client.send("🔒 Nickname Lock Active!", thread_id, thread_type)
        
        elif msg == "+nicklock off":
            self.nicklock_active = False
            self.client.send("🔓 Nickname Lock Disabled!", thread_id, thread_type)

    # --- AUTO ENFORCER (Ye check karega ki lock ON hai ya nahi) ---
    def handle_title_change(self, author_id, thread_id, thread_type):
        if self.namelock_active and author_id != OWNER_ID:
            time.sleep(1.2)
            self.client.changeThreadTitle(self.locked_title, thread_id=thread_id, thread_type=thread_type)
            self.client.sendRemoteImage(SUKUNA_IMG, message="⚠️ Yuvi ka lock laga hai! Naam mat badlo.", thread_id=thread_id, thread_type=thread_type)

    def handle_nick_change(self, author_id, changed_for, thread_id, thread_type):
        if self.nicklock_active and author_id != OWNER_ID:
            time.sleep(1.2)
            self.client.changeNickname("Locked by Yuvi", changed_for, thread_id=thread_id, thread_type=thread_type)
