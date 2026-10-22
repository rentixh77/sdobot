import imaplib
import email
from email.header import decode_header
import time
import subprocess

server = ".."
username = ".."              #Ваш id для входа в систему.
password = ".."                            #Ваш пароль для входа в систему.

def decode_value(value):
    if not value:
        return None
    dh = decode_header(value)
    return "".join(
        part.decode(enc or "utf-8") if isinstance(part, bytes) else part
        for part, enc in dh
    )
def process_mail():
    imap = imaplib.IMAP4_SSL(server)
    imap.login(username, password)

    imap.select("bot")                      #Создаете папку с названием "bot" в почте. Или любую другую НА ЛАТИНИЦЕ и меняете эту строку.


    st, data = imap.search(None, 'unseen')
    ids = data[0].decode().split()

    for uid in ids:
        st, msg = imap.fetch(uid, '(BODY.PEEK[HEADER.FIELDS (SUBJECT FROM)])')
        raw_bytes = msg[0][1]

        msg_obj = email.message_from_bytes(raw_bytes)

        subject = decode_value(msg_obj["Subject"])
        sender = decode_value(msg_obj["From"])

        imap.store(uid, '+FLAGS', '\\Seen')

        subprocess.call([
            "python3",
            "telegram_sender.py",           #Отправка данных с почты в telegram_sender.py
            subject if subject else "",
            sender if sender else ""
        ])

    imap.logout()

while True:
    process_mail()
    time.sleep(20)                          #Проверка раз в 20 секунд.
