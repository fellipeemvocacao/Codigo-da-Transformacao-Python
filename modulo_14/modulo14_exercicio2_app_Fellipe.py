from flask import Flask, render_template, request, redirect, url_url_for, flash

app = Flask(__name__)
app.secret_key = "chave_secreta_para_alertas"

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 4500.00, "quantidade": 10},
    {"id": 2, "nome": "Mouse Sem Fio", "preco": 89.90, "quantidade": 50}
]
proximo_id = 3

@app.route('/')
def listar_produtos():
    return render_template('listar.html', produtos=produtos)

@app.route('/produto/novo', methods=['GET', 'POST'])
def cadastrar_produto():
    global proximo_id
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = float(request.form.get('preco'))
        quantidade = int(request.form.get('quantidade'))
        
        novo_produto = {
            "id": proximo_id,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(novo_produto)
        proximo_id += 1
        
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for('listar_produtos'))
        
    return render_template('cadastrar.html')

@app.route('/produto/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    
    if not produto:
        flash("Produto não encontrado!", "danger")
        return redirect(url_for('listar_produtos'))
        
    if request.method == 'POST':
        produto['nome'] = request.form.get('nome')
        produto['preco'] = float(request.form.get('preco'))
        produto['quantidade'] = int(request.form.get('quantidade'))
        
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for('listar_produtos'))
        
    return render_template('editar.html', produto=produto)

@app.route('/produto/excluir/<int:id>', methods=['POST'])
def excluir_produto(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    app.run(debug=True)