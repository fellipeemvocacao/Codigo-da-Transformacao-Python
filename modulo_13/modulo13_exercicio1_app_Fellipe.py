from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    
    return jsonify({
        "mensagem": f"Olá, {nome}! Seja bem-vindo à API.",
        "status": "sucesso"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)