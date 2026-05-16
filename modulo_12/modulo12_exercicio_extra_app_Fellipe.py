from flask import Flask, jsonify, request

app = Flask(__name__)
PRODUTOS = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 350.0}
]

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(PRODUTOS), 200

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400
        
    novo_produto = {
        "id": len(PRODUTOS) + 1,
        "nome": dados["nome"],
        "preco": dados["preco"]
    }
    PRODUTOS.append(novo_produto)
    return jsonify(novo_produto), 201

if __name__ == '__main__':
    app.run(debug=True)