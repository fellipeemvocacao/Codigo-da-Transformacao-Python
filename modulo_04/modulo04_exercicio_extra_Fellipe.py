def sistema_agenda():
    agenda = {}

    while True:
        print("\n--- 📱 AGENDA DE CONTATOS ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Todos")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do contato: ").strip().title()
            telefone = input("Telefone: ").strip()
            agenda[nome] = telefone
            print(f"✅ Contato '{nome}' salvo!")

        elif opcao == "2":
            nome = input("Nome para remover: ").strip().title()
            removido = agenda.pop(nome, None)
            if removido:
                print(f"🗑️ Contato '{nome}' removido.")
            else:
                print("⚠️ Contato não encontrado.")

        elif opcao == "3":
            nome = input("Buscar por nome: ").strip().title()
            if nome in agenda:
                print(f"📞 Telefone de {nome}: {agenda[nome]}")
            else:
                print("⚠️ Nome não consta na agenda.")

        elif opcao == "4":
            if not agenda:
                print("📭 A agenda está vazia.")
            else:
                print("\n--- Lista de Contatos ---")
                for nome, telefone in agenda.items():
                    print(f"👤 {nome}: {telefone}")

        elif opcao == "5":
            print("Encerrando agenda...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    sistema_agenda()