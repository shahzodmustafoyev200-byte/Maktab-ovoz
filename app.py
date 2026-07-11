from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ism = request.form.get("ism")
        fikr = request.form.get("fikr")

        message = f"📩 Yangi murojaat\n\nIsm: {ism}\nFikr: {fikr}"

        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            telegram_url,
            data={
                "chat_id": CHAT_ID,
                "text": message
            }
        )

        return "Fikringiz yuborildi. Rahmat!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
