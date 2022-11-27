#!/bin/python3
import flask, flask_login
from flask import url_for, request, render_template, redirect
from flask_login import current_user
from flask_sock import Sock
import collections, json, queue, random
from datetime import datetime
from base import app,load_info,ajax,DBDict,DBList,random_id,hash_id,full_url_for

# -- Info for every Hack-A-Day project --
load_info({
    "project_name": "Hack-A-Minigame",
    "source_url": "https://github.com/za3k/day26_mini",
    "subdir": "/hackaday/mini",
    "description": "A very tiny minigame, where your only controls are save/restore. To play yourself, visit <a href=\"https://tilde.za3k.com/hackaday/snake\">Hack-A-Snake</a>",
    "instructions": "This is the classic game Snake, played by an AI pressing random buttons. Your only power is to save and load the game, using three save slots.",
    "login": True,
    "fullscreen": False,
})

# -- Routes specific to this Hack-A-Day project --

@app.route("/")
def index():
    return render_template('index.html')
