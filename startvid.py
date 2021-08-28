import flask
from flask import Blueprint
import json
import os

startvid = Blueprint("start_vid", "")


@startvid.route("/startvid", methods=['POST'])
def yt_startvid():
    try:
        url = flask.request.form["url"]
    except Exception as e:
        print(e)
        url = json.loads(flask.request.data)["url"]

    print(f"Request to open url {url}")
    os.system("taskkill /F /IM chrome.exe")
    os.system(f"chrome --kiosk {url}")

    return ""
