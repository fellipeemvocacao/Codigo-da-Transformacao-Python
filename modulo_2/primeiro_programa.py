print("Olá, mundo!")

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
idade = int(input("Digite sua idade: "))
print(f"Olá, {nome}! Você tem {idade} anos.")

if idade <= 18:
    print('Jovem é menor de idade')

elif idade <= 65:
    print('Jovem é adulto, é maior de idade')

else:
    print('Jovem é idoso de idade')