import json

def load_test_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)