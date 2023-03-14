from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get("https://josep-da-humble-disco-9rx45px9vwq277gq-8080.preview.app.github.dev/home")
    print(r)
    print(r.text)
    return r.text

if __name__ == "__main__":
    app.run(debug=True)