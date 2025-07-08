import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_notification(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)
if __name__ == "__main__":

    send_telegram_notification("🚨 This is a test flight alert!")
