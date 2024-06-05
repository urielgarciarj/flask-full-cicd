from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!!"

@app.route('/health')
def health_check():
    return "Healthy!"

@app.route('/users/<user_id>')
def get_user(user_id):
    user = {
        "id": user_id,
        "name": "Alice",
        "email": "Alice@gmail.com"
    }
    query = request.args.get('query')
    if query:
        user['query'] = query
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        "id": data['id'],
        "name": data['name'],
        "email": data['email']
    }
    return jsonify(user), 201


if __name__ == '__main__':
    app.run(debug=True)