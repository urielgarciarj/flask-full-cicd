from flask import Blueprint, request, jsonify

import traceback
import json
import os

main = Blueprint('list_blueprint', __name__)

current_dir = os.path.dirname(os.path.abspath(__file__)) # /home/uriel/uriel/repos/flask-full-cicd/src/routes
data_file_path = os.path.join(current_dir, 'data.json') # /home/uriel/uriel/repos/flask-full-cicd/src/routes/data.json

@main.route('/', methods=['GET'])
def index():
    try:
        with open(data_file_path) as file:
            data = json.load(file)
            # Use the data as needed
            return jsonify(data)
    except FileNotFoundError:
        traceback.print_exc()
        return "Error: data.json file not found"
    except Exception:
        traceback.print_exc()
        return "Error: Failed to read data.json"