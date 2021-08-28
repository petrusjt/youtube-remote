import flask
from flask import Blueprint
import json
from pynput.keyboard import Controller, Key
from util.tap_key import tap_key

keyboard = Controller()


def next():
    global keyboard
    with keyboard.pressed(Key.shift):
        tap_key(keyboard, 'n')


def previous():
    global keyboard
    with keyboard.pressed(Key.shift):
        tap_key(keyboard, 'p')


actions = {
    "play/pause": lambda: tap_key(keyboard, Key.space),
    "fullscreen": lambda: tap_key(keyboard, 'f'),
    "volume+": lambda: tap_key(keyboard, Key.up),
    "volume-": lambda: tap_key(keyboard, Key.down),
    "back10": lambda: tap_key(keyboard, 'j'),
    "forward10": lambda: tap_key(keyboard, 'l'),
    "mute": lambda: tap_key(keyboard, 'm'),
    "next": next,
    "previous": previous
}

yt_player_actions = Blueprint("player_actions", "")


@yt_player_actions.route("/player-action", methods=['POST'])
def player_actions():
    global keyboard
    try:
        action = flask.request.form["action"]
    except Exception as e:
        print(e)
        action = json.loads(flask.request.data)["action"]
    print(f"Request to {action}")
    actions[action]()

    return ""
