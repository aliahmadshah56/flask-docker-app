from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Flask REST API is running!",
        "status": "healthy"
    })

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Laptop", "price": 150000},
        {"id": 2, "name": "Mouse",  "price": 2500},
        {"id": 3, "name": "Keyboard","price": 4000}
    ]
    return jsonify({"items": items, "total": len(items)})

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    return jsonify({
        "message": "Item added successfully",
        "item": data
    }), 201

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
