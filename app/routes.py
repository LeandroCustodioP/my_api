from flask import jsonify, request
from app import app

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status":"API is running!"})

@app.route('/api/data', methods=['POST'])
def get_data():
    # Obtenha os dados JSON do corpo da requisição
    data = request.get_json()  # Certifique-se de que 'data' está definido
    return jsonify({"received_data":data})