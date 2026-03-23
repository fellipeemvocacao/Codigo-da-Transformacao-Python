tarefas = []

print("--- BEM-VINDO AO GERENCIADOR DE TAREFAS ---")

while True:
    
    tarefas.sort()
    print(f"\nLista atual: {tarefas}")
    
    comando = input("Digite uma tarefa, 'remover' para excluir, ou 'sair': ")
    
    if comando.lower() == 'sair':
        break
        
    elif comando.lower() == 'remover':
        if len(tarefas) > 0:
            item_para_remover = input("Qual tarefa deseja remover? ")
            if item_para_remover in tarefas:
                tarefas.remove(item_para_remover)
                print(f"🗑️ '{item_para_remover}' removida com sucesso!")
            else:
                print(f"❌ Erro: '{item_para_remover}' não encontrada.")
        else:
            print("⚠️ A lista já está vazia.")
            
    elif comando != "":
        tarefas.append(comando)
        
        tarefas.sort()
        print(f"✅ '{comando}' adicionada!")
    else:
        print("⚠️ Você não digitou nada.")


tarefas.sort()
print("\n--- LISTA FINAL (A-Z) ---")
for i, t in enumerate(tarefas, 1):
    print(f"{i}. {t}")