numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')
operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /, 5 -> %: ')


if operar_numb == '5':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
elif operar_numb == '4':
    if int(numb_dois) != 0:
        result = int(numb_hum) / int(numb_dois)
        print(f'O resultado é: {result}')
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operar_numb == '3':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '2':
    result = int(numb_hum) - int(numb_hum)
    print(f'O resultado é: {result}')

elif operar_numb == '1':
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')
    

else:
    print("Número não é válido, tente novamente!")