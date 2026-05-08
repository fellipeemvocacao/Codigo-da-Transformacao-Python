def gerenciar_compras():
    lista_compras = []
    
    while True:
        print("\n--- 🛒 MINHA LISTA DE COMPRAS ---")
        if not lista_compras:
            print("Sua lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        
        print("-" * 30)
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Finalizar e Sair")
        
        opcao = input("\nEscolha uma ação: ")

        if opcao == "1":
            item = input("Digite o nome do item: ").strip().capitalize()
            if item:
                lista_compras.append(item)
                print(f"✅ '{item}' adicionado!")
        
        elif opcao == "2":
            if not lista_compras:
                print("⚠️ Nada para remover.")
                continue
            
            try:
                indice = int(input("Digite o número do item para remover: ")) - 1
                removido = lista_compras.pop(indice)
                print(f"🗑️ '{removido}' removido com sucesso!")
            except (ValueError, IndexError):
                print("❌ Erro: Número inválido.")

        elif opcao == "3":
            print("Saindo... Boas compras!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    gerenciar_compras()