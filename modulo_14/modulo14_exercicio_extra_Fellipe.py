from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

@app.route('/produtos')
def listar_produtos():
    termo_busca = request.args.get('q', default='', type=str)
    pagina_atual = request.args.get('page', default=1, type=int)
    items_por_pagina = 5  

    query = Produto.query

    if termo_busca:
        query = query.filter(Produto.nome.ilike(f'%{termo_busca}%'))

    paginacao = query.paginate(page=pagina_atual, per_page=items_por_pagina, error_out=False)

    return render_template('produtos.html', paginacao=paginacao, busca=termo_busca)

if __name__ == '__main__':
    app.run(debug=True)