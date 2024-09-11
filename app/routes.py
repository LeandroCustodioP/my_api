from flask import jsonify, request
from app import app, db
from app.models import  User
from marshmallow import ValidationError
from app.schemas import UserSchema

user_schema = UserSchema()

# Endpoint para criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Valida os dados recebidos
        data = user_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Criar o usuário se os dados forem válidos
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

# Endpoint para listar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

# Endpoint para obter os detalhes de um usuário específico
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

# Endpoint para atualizar as informações de um usuário
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return jsonify({"message": "User updated successfully!"})

# Endpoint para excluir um usuário
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully!"})

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status":"API is running!"})

@app.route('/api/data', methods=['POST'])
def get_data():
    # Obtenha os dados JSON do corpo da requisição
    data = request.get_json()  # Certifique-se de que 'data' está definido
    return jsonify({"received_data":data})