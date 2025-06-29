from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (replace with a database in a real app)
items = []
next_id = 1

# Create (POST /items)
@app.route('/items', methods=['POST'])
def create_item():
    global next_id
    data = request.get_json()
    new_item = {
        'id': next_id,
        'name': data['name'],
        'quantity': data['quantity']
    }
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201

# Read all (GET /items)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Read one (GET /items/<id>)
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

# Update (PUT /items/<id>)
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = data.get('name', item['name'])
    item['quantity'] = data.get('quantity', item['quantity'])
    return jsonify(item)

# Delete (DELETE /items/<id>)
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)