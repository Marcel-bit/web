from flask import Flask, render_template, request
import requests
from tinydb import TinyDB, Query

db = TinyDB('db.json')
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(request.remote_addr)
    klic = requests.get("https://api.chucknorris.io/jokes/random").json()
    tole = (klic["value"])
    db.insert({'vic': tole})
    return render_template("index.html", spremenljivka = tole, elements = list(range(10)))


@app.route("/data")
def test():
    klic = requests.get("https://api.chucknorris.io/jokes/random").json()
    return klic["value"]
    


app.run(debug=True, port=8080)
