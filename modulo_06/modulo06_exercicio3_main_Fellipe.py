from banco_dados.gerenciador_csv import salvar_nota, carregar_notas
from interface.formatacao import exibir_titulo 

def sistema_notas():
    exibir_titulo("Sistema de Notas Acadêmicas")
    
    while True:
        print("\n1. Adicionar Nota")
        print("2. Ver Todas as Notas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Aluno: ")
            materia = input("Disciplina: ")
            try:
                valor_nota = float(input("Nota: "))
                salvar_nota(nome, materia, valor_nota)
                print("✅ Nota salva com sucesso!")
            except ValueError:
                print("❌ Erro: Digite um número válido para a nota.")
        
        elif opcao == "2":
            dados = carregar_notas()
            if not dados:
                print("\nNenhuma nota registrada ainda.")
            else:
                print(f"\n{'ALUNO':<20} | {'DISCIPLINA':<15} | {'NOTA':<5}")
                print("-" * 45)
                for item in dados:
                    print(f"{item['Nome']:<20} | {item['Disciplina']:<15} | {item['Nota']:<5}")
        
        elif opcao == "3":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    sistema_notas()