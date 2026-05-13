import sqlite3

def conectar():
    return sqlite3.connect('empresa.db')

def inserir_cliente(nome, email):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"✅ Cliente '{nome}' inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"❌ Erro: O e-mail '{email}' já está cadastrado.")
    finally:
        conn.close()

def consultar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conn.close()
    
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | E-mail: {c[2]}")
    print("-------------------------\n")

def atualizar_email(id_cliente, novo_email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"🔄 Cliente ID {id_cliente} atualizado para: {novo_email}")
    else:
        print(f"⚠️ Cliente ID {id_cliente} não encontrado.")
    conn.close()

def deletar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"🗑️ Cliente ID {id_cliente} removido com sucesso.")
    else:
        print(f"⚠️ Cliente ID {id_cliente} não encontrado.")
    conn.close()


if __name__ == "__main__":
    inserir_cliente("Alice Silva", "alice@email.com")
    inserir_cliente("Bob Souza", "bob@email.com")
    consultar_clientes()
    atualizar_email(1, "alice.nova@email.com")
    deletar_cliente(2)
    consultar_clientes()