class InfoCommand:
    def __init__(self, client):
        self.client = client

    def send_info(self, thread_id, thread_type):
        # Yahan apna Render wala link daal dena
        dashboard_url = "https://yuvi-war-bot.onrender.com" 
        
        info_text = f"""
◆ YUVI VERMA BOT INFO ◆

👤 OWNER: YUVI VERMA
🛡️ STATUS: PROTECTED MODE
🚀 SYSTEM: ONLINE

🌐 MERA PERSONAL PAGE:
👉 {dashboard_url}
"""
        # Aapki pasand ki koi bhi image link yahan daal sakte ho
        img_url = "https://i.ibb.co/WvHj4HZP/IMG-20260404-191841.png"
        self.client.sendRemoteImage(img_url, message=info_text, thread_id=thread_id, thread_type=thread_type)

