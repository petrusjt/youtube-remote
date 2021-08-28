import flask
from flask import Blueprint

index = Blueprint("page", "index", static_folder="static",
                  template_folder="template")


@index.route('/', methods=['GET'])
def home():
    return flask.render_template("index.html")
