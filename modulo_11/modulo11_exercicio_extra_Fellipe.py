import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conexao.commit()
    return conexao

def adicionar_tarefa(conexao, descricao):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao,))
    conexao.commit()
    print(f"\n✅ Tarefa '{descricao}' adicionada com sucesso!")

def visualizar_tarefas(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    
    if not tarefas:
        print("\n📭 Nenhuma tarefa pendente.")
    else:
        print("\n--- LISTA DE TAREFAS ---")
        for tarefa in tarefas:
            status = "[X]" if tarefa[2] else "[ ]"
            print(f"{tarefa[0]}. {status} {tarefa[1]}")
        print("------------------------")

def excluir_tarefa(conexao, id_tarefa):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"\n🗑️ Tarefa {id_tarefa} removida!")
    else:
        print("\n⚠️ ID não encontrado.")

def menu():
    conexao = inicializar_banco()
    
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Excluir Tarefa")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            desc = input("Descrição da tarefa: ")
            adicionar_tarefa(conexao, desc)
        elif opcao == '2':
            visualizar_tarefas(conexao)
        elif opcao == '3':
            visualizar_tarefas(conexao)
            try:
                id_remocao = int(input("Digite o ID da tarefa para excluir: "))
                excluir_tarefa(conexao, id_remocao)
            except ValueError:
                print("❌ Por favor, digite um número válido.")
        elif opcao == '4':
            print("Encerrando... Até logo!")
            conexao.close()
            break
        else:
            print("🚫 Opção inválida!")

if __name__ == "__main__":
    menu()