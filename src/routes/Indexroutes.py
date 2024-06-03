from flask import Blueprint, request, jsonify, Flask

import traceback

main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    return "Hello, World!!!! from index"