from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ism = request.form.get("ism")
        fikr = request.form.get("fikr")

        with open("fikrlar.txt", "a", encoding="utf-8") as f:
            f.write(f"Ism: {ism}\nFikr: {fikr}\n---\n")

        return "Fikringiz yuborildi. Rahmat!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
