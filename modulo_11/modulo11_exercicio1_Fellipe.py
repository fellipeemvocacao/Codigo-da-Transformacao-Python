import sqlite3
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

conexao.commit()
conexao.close()
print("Banco de dados e tabela 'Clientes' criados com sucesso!")