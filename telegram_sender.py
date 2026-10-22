import sys
import requests

BOT_TOKEN = ".."           #Сюда вставляете токен бота (берется в Bot Father)
CHAT_ID = ""             #Сюда вставляете id чата (берется с сайта api.telegram.org/bot<ТОКЕН_БОТА>/getUpdates)

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)
def main():
    if len(sys.argv) < 3:
        print("Not enough args")
        return

    subject = sys.argv[1]
    sender = sys.argv[2]

    msg = f"Новое сообщение:\nОт: {sender}\nТема: {subject}"

    send(msg)

if __name__ == "__main__":
    main()
