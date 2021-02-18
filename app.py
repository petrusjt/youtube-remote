import flask
import os
from pynput.keyboard import Key, KeyCode, Controller
import pynput.mouse as mouse
from time import sleep

def tap_key(controller, key):
    controller.press(key)
    controller.release(key)

app = flask.Flask(__name__, static_folder="static", template_folder="template")

keyboard = Controller()

ms = mouse.Controller()

@app.route("/", methods=['GET'])
def home():
    return flask.render_template("index.html")

@app.route("/youtube/startvid", methods=['POST'])
def yt_startvid():

    url = flask.request.form["url"]
    #print(flask.request.json)
    print(f"Request to open url {url}")
    os.system("taskkill /F /IM chrome.exe")
    os.system(f"chrome {url}")
    
    sleep(5)
    # Edit the coordinates at the next line to match your monitor's
    ms.position = (2542, 80)
    #
    print(f"mouse position: {ms.position}")
    ms.click(mouse.Button.left, 1)

    return ""

@app.route("/youtube/player-action", methods=['POST'])
def yt_player_action():
    global keyboard
    action = flask.request.form["action"]

    print(f"Request to {action}")

    if action == "play/pause":
        tap_key(keyboard, Key.space)
    elif action == "fullscreen":
        tap_key(keyboard, "f")
    elif action == "volume+":
        tap_key(keyboard, Key.up)
    elif action == "volume-":
        tap_key(keyboard, Key.down)
    elif action == "back10":
        tap_key(keyboard, "j")
    elif action == "forward10":
        tap_key(keyboard, "l")
    elif action == "mute":
        tap_key(keyboard, "m")
    elif action == "next":
        with keyboard.pressed(Key.shift):
            tap_key(keyboard, "n")
    elif action == "previous":
        with keyboard.pressed(Key.shift):
            tap_key(keyboard, "p")


    return ""

app.run(host="0.0.0.0", port=80)