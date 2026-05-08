def menu_calculadora():
    while True:
        print("\n" + "="*25)
        print("   🔢 MENU DE OPERAÇÕES")
        print("="*25)
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Sair")
        print("="*25)

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "4":
            print("Encerrando o programa. Até logo!")
            break 
        
        if opcao in ("1", "2", "3"):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    resultado = num1 + num2
                    simbolo = "+"
                elif opcao == "2":
                    resultado = num1 - num2
                    simbolo = "-"
                elif opcao == "3":
                    resultado = num1 * num2
                    simbolo = "*"
                
                print(f"\n✅ Resultado: {num1} {simbolo} {num2} = {resultado}")
            
            except ValueError:
                print("\n❌ Erro: Por favor, digite apenas números.")
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_calculadora()