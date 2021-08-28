import flask
from index import index
from startvid import startvid
from yt_player_actions import yt_player_actions

app = flask.Flask(__name__, static_folder="static", template_folder="template")
app.register_blueprint(index)
app.register_blueprint(startvid, url_prefix="/youtube")
app.register_blueprint(yt_player_actions, url_prefix="/youtube")
app.run(host="0.0.0.0", port=80)
