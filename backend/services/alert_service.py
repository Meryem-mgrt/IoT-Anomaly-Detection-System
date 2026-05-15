# telegram/email

import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_alert(message: str, severity: str = "medium"):
    """
    Sends alert to Telegram (MVP version)
    """

    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Alert system not configured")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"[{severity.upper()}] {message}"
    }

    try:
        requests.post(url, json=payload)
        print("🚨 Alert sent")
    except Exception as e:
        print("Alert failed:", e)