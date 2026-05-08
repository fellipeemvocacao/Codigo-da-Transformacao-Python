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