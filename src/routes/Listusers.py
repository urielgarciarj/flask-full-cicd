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
    
@main.route('/<int:user_id>', methods=['GET'])
def user_by_id(user_id):  # Add the missing parameter user_id
    try:
        with open(data_file_path) as file:
           data = json.load(file)
        print(f"Data: {data}")  # Debug print
        for data_item in data:
            print(f"Data item: {data_item}")  # Debug print
            if data_item['id'] == int(user_id):
                print(data_item)
                return jsonify(data_item)
    except Exception:
        traceback.print_exc()
        return "Error: Failed to add data"