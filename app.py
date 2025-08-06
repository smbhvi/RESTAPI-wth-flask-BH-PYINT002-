from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@app.route('/')
def home():
    return jsonify({"message": "User Management API"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user if user else {"error": "User not found"}), 200 if user else 404

if __name__ == '__main__':
    app.run(debug=True)
