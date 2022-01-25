import json

from flask import jsonify, send_from_directory, request, Response
from src import app
from src import dao


@app.route("/")
def index():
    return send_from_directory("client/public", "index.html")


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory("client/public", path)


@app.route("/save_as", methods=["POST"])
def save_as():
    payload = request.json
    save_as_name = payload.pop("saveAsName")
    match_data = {**payload, "info": json.loads(payload["info"])}
    dao.save_match(match_data, save_as_name)
    print(f'Saved "{save_as_name}" slot')
    return Response(status=201)


@app.route("/slots", methods=["GET"])
def get_slots():
    return jsonify(dao.get_slots())


@app.route("/load_match/<name>", methods=["GET"])
def load_match(name):
    return jsonify(dao.load_match(name))


@app.route("/delete_slot", methods=["POST"])
def delete_slot():
    payload = request.json
    name = payload.pop("name")
    dao.delete_slot(name)
    print(f'Deleted "{name}" slot')
    return Response(status=201)
