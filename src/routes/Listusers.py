from flask import Blueprint, request, jsonify

import traceback

main = Blueprint('list_blueprint', __name__)


@main.route('/', methods=['GET'])
def index():
    return "Hello, World from list users"