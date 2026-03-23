'''

nota = 100
if nota>90:
    print('Nota A')
elif nota>80:
    print('Nota B')
elif nota>70:
    print('Nota C')
else:
    print('Reprovado')
    


for i in range(1):
   print(f"Iteração {i}")
   contador = 0
while contador < 26:
   print(f"Contador: {contador}")
   contador +=2

'''



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
    


num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1 > num2:
    print(f" O maior número é o {num1}")
elif num1 < num2:
    print(f" O maior número é o {num2}")
else:
    print("Os dois números são iguais")


idade_pessoa = int(input('Digite sua idade: '))

if idade_pessoa <= 18:
    print('Você é uma criança')

elif idade_pessoa > 18 and idade_pessoa < 20:
    print('Você é um jovem maior de 18 anos')

elif idade_pessoa >= 20 and idade_pessoa < 60:
    print('Você é uma pessoa adulta')

elif idade_pessoa > 60:
    print('Você é uma pessoa idosa')

else:
    print('Digite novamente')