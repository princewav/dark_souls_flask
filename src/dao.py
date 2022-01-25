from pathlib import Path
import json
from pprint import pprint

from src import app


def save_match(json_string, save_slot_name):
    with (app.config["DATA_PATH"] / f"{save_slot_name}.json").open("w") as f:
        json.dump(json_string, f)


def get_slots():
    return [
        {**json.loads(x.read_text()), "name": x.name[:-5]}
        for x in app.config["DATA_PATH"].iterdir()
    ]


def delete_slot(slot_name):
    (app.config["DATA_PATH"] / f'{slot_name}.json').unlink()


def load_match(save_slot_name):
    with Path(f"./data/{save_slot_name}.json").open() as f:
        json_string = json.load(f)
    return json_string


def main():
    delete_slot('sus')


if __name__ == "__main__":
    main()
