'''

CRUD

Padaria

O sistema da padaria deve permitir o acesso ao menu de produtos e promoções, onde o cliente pode selecionar 
os itens desejados e adiciona-los ao pedido. O sistema deve calcular o valor do pedido de acordo com o valor
do produto selecionado. O sistema deve permitir que o cliente possa finalizar o pedido, e escolher entre a
retirada no estabelecimento ou a entrega. E, então, escolher o método de pagamento, onde o cliente possa escolher entre 
dinheiro, pix, ou cartão de crédito ou débito. O sistema deve confirmar se o pedido chegou ao estabelecimento.

'''

print('Padaria Peter Pão - o melhor pão da cidade! 🥞🥐🥖')

nome_gentil = input('Qual é o seu nome?: ')
print(f"Olá, {nome_gentil}! Seja bem-vindo(a) à nossa padaria!")

total_conta = 0.0  
carrinho = []

while True:
    print("\n" + "="*28)
    print("--- MENU PADARIA ---")
    print("1 - Entrar\n2- Fazer cadastro\n3- Ver o cardápio e Pedir\n4- Meus pedidos / Total\n5- Informações da loja")
    print("0- Sair")
    print(f"💰 Total acumulado: R${total_conta:.2f}")
    print("="*28)

    acesso_menu = input("\nO que você quer fazer?: ")

    
    if acesso_menu == "1":
        print("\n--- ENTRAR ---")
        def realizar_login_seguro():
         senha_padrao = "1234"

         print('\n--- Sistema de Login Seguro ---')
         nome_usuario = input('Digite seu login: ')
         senha_digitada = input('Digite sua senha: ')
         if senha_digitada == senha_padrao:
           print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}! Acesso concedido.')
         else:
          print('\n[ERRO] Senha incorreta! Acesso negado.')

        print('---------------------------\n')

        realizar_login_seguro()
    
    
    elif acesso_menu == "2":
        print("\n--- FAZER CADASTRO ---")
        email_cliente = input("Digite o seu email: ")
        endereco_cliente = input("Digite o seu endereço: ")
        cpf_cnpj_cliente = input("Digite o seu CPF/CNPJ: ")
        telefone_cliente = input("Digite o seu telefone: ")
        print("✅ Cadastro realizado com sucesso!")

    elif acesso_menu == "3":
        print("\n--- CARDÁPIO ---")
        print("1- Salgados\n2- Doces\n3- Bebidas\n4- Promoções")
        categoria = input("Escolha uma categoria: ")

        if categoria == "1":
            print("\n[SALGADOS]\n1-Coxinha (R$5)\n2-Kibe (R$6)\n3-Empada (R$4)\n4-Esfiha (R$5)\n5-Pão de Queijo (R$3)\n6-Pão Francês (R$2)\n7-Torta Frango (R$8)")
            item = input("Digite o NÚMERO do produto: ")
            
            
            nomes = {"1": "Coxinha", "2": "Kibe", "3": "Empada", "4": "Esfiha", "5": "Pão de Queijo", "6": "Pão Francês", "7": "Torta de Frango"}
            precos = {"1": 5.0, "2": 6.0, "3": 4.0, "4": 5.0, "5": 3.0, "6": 2.0, "7": 8.0}
            
            if item in precos:
                total_conta += precos[item]
                carrinho.append(nomes[item]) 
                print(f"✅ {nomes[item]} adicionado! Subtotal: R${total_conta:.2f}")
            else:
                print("❌ Número inválido.")

        elif categoria == "2":
            print("\n[DOCES]\n8-Brigadeiro (R$3)\n9-Beijinho (R$3)\n10-Pudim (R$5)\n11-Tortas (R$8)\n12-Sonho (R$6)\n13-Bolos (R$11)")
            item = input("Digite o NÚMERO do produto: ")
            
            nomes = {"8": "Brigadeiro", "9": "Beijinho", "10": "Pudim", "11": "Torta", "12": "Sonho", "13": "Bolo"}
            precos = {"8": 3.0, "9": 3.0, "10": 5.0, "11": 8.0, "12": 6.0, "13": 11.0}
            
            if item in precos:
                total_conta += precos[item]
                carrinho.append(nomes[item])
                print(f"✅ {nomes[item]} adicionado! Subtotal: R${total_conta:.2f}")

        elif categoria == "4":
            print("\n[BEBIDAS]\n14-Sucos (R$4)\n15-Refrigerante (R$5)\n16-Café (R$3)")
            item = input("Digite o NÚMERO do produto: ")
            
            nomes = {"14": "Suco", "15": "Refrigerante", "16": "Café"}
            precos = {"14": 4.0, "15": 5.0, "16": 3.0}
            
            if item in precos:
                total_conta += precos[item]
                carrinho.append(nomes[item])
                print(f"✅ {nomes[item]} adicionado! Subtotal: R${total_conta:.2f}")

        elif categoria == "5":
            print("\n[PROMOÇÕES]\n17-Combo 1 - Coxinha + Suco (R$8)\n18-Combo 2 - Torta + Refrigerante (R$12)\n19-Combo 3 - Esfiha + Suco (R$7)")
            item = input("Digite o NÚMERO do produto: ")
            
            nomes = {"17": "Combo 1", "18": "Combo 2", "19": "Combo 3"}
            precos = {"17": 8.0, "18": 12.0, "19": 7.0}
            
            if item in precos:
                total_conta += precos[item]
                carrinho.append(nomes[item])
                print(f"✅ {nomes[item]} adicionado! Subtotal: R${total_conta:.2f}")

        input("\nAperte ENTER para continuar...")

    elif acesso_menu == "4":
        print("\n--- RESUMO DO PEDIDO ---")
        print(f"💵 Valor total a pagar: R${total_conta:.2f}")
        print("Status: 1-Pagar / 2-Ver Itens / 3-Voltar")
        opcao_pedido = input("\nO que você quer fazer?: ")

        if opcao_pedido == '1':
            if total_conta > 0:
                print("\n1 - Cartão\n2 - Pix")
                metodo_pagamento = input("Escolha a forma de pagamento: ")
                
                if metodo_pagamento == '1':
                    print("\n[CARTÃO]")
                    print("1 - Débito\n2 - Crédito\n3 - Vale alimentação\n4 - Cartão Pré-pago")
                    cartao_tipo = input("Digite qual tipo de cartão: ")
                    tipos = {"1": "Débito", "2": "Crédito", "3": "Vale Alimentação", "4": "Pré-pago"}
                    nome_cartao = tipos.get(cartao_tipo, "Cartão Desconhecido")
                    
                    print(f"\nMétodo selecionado: {nome_cartao}")
                    print("⌛ Processando... Aproxime o cartão... Pagamento em análise...")
                    print("✅ Pagamento realizado com sucesso! Obrigado por comprar em nossa padaria. Volte sempre!")
                    total_conta = 0 
                    carrinho = [] 
                
                elif metodo_pagamento == '2':
                    print("\n--- PIX ---")
                    print("Pague via QR-code ou pela chave Aleatória: 123e4567-e89b-12d3-a456-426614174000/n⌛ Processando...")
                    print("✅ Pagamento confirmado via PIX! Obrigado por comprar em nossa padaria. Volte sempre!")
                    total_conta = 0
                    carrinho = [] 
            else:
                print("⚠️ Seu carrinho está vazio!")

        elif opcao_pedido == '2':
            if len(carrinho) > 0:
                print("\n--- ITENS NO CARRINHO ---")
                
                for i, produto in enumerate(carrinho, 1):
                    print(f"{i}. {produto}")
                print(f"\nTotal de itens: {len(carrinho)}")
                print(f"R${total_conta:.2f}")
            else:
                print("\n🛒 O carrinho está vazio.")
            input("\nAperte ENTER para voltar...")

        elif opcao_pedido == '3':
            print("Voltando para o menu principal")

    elif acesso_menu == "5":
        print("\n--- INFORMAÇÕES ---")
        print("📍 Rua dos Pães, 123 - Centro - 🔗 Veja no Mapa: https://maps.google.com/?q=Padaria+Peter+Pao\n📞 (11) 1234-5678\nHorário de funcionamento: Segunda a sábado, das 6h às 20h")
        print("Acesse nosso site: https://www.padariapeterpao.com.br")

    elif acesso_menu == "0":
        print(f"\nSaindo... Tchau, {nome_gentil}, Obrigado pela visita!")
        break
    
    else:
        print("\n❌ Opção inválida.")