from flask import send_from_directory, request, Response
from src import app
from src import dao


# Path for our main Svelte page


@app.route("/")
def index():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/save_as", methods=['POST'])
def save_as():
    payload = request.json
    print(f'Payload:  {payload}')
    save_as_name = payload['name']
    match_data = payload['match_data']
    dao.save_match(match_data, save_as_name)
    print(f'Saved {save_as_name} slot')
    return Response(status=201)
