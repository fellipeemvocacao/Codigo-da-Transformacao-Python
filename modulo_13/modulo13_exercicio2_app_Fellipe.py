from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    
    if not dados:
        return jsonify({"erro": "Corpo da requisição vazio ou formato inválido"}), 400
        
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    
    if not nome or not email or not senha:
        return jsonify({"erro": "Campos obrigatórios ausentes (nome, email, senha)"}), 400
        
    usuario_criado = {
        "id": 101,
        "nome": nome,
        "email": email
    }
    
    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario": usuario_criado
    }), 201

if __name__ == '__main__':
    app.run(port=3000, debug=True)