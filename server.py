from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>UwU</h1><p>Wie sie sehen, siehen sie nichts</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 5000 ist Standard für Flask