def saudar_usuario(nome):
    print(f"Olá, {nome}! Seja bem-vindo ao nosso sistema.")

def calcula_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    status = "Aprovado" if media >= 7 else "Reprovado. Sinto muito"
    return media, status

def maior_menor(n1, n2, n3, n4):
    maior = max(n1, n2, n3, n4)
    menor = min(n1, n2, n3, n4)
    return maior, menor
if calcula_media:
    nome_aluno = input("Digite o seu nome: ")
    saudar_usuario(nome_aluno)

    nota1 = float(input("Digite sua nota do 1° Bimestre: "))
    nota2 = float(input("Digite sua nota do 2° Bimestre: "))
    nota3 = float(input("Digite sua nota do 3° Bimestre: "))
    nota4 = float(input("Digite sua nota do 4° Bimestre: "))

    resultado, status = calcula_media(nota1, nota2, nota3, nota4)
    maior_nota, menor_nota = maior_menor(nota1, nota2, nota3, nota4)

    print("\n" + "=" * 30)
    print(f"RELATÓRIO DO ALUNO: {nome_aluno.upper()}")
    print("-" * 30)
    print(f"Média Final: {resultado:.1f}") 
    print(f"Status: {status}")
    print(f"Maior Nota: {maior_nota:.1f}")
    print(f"Menor Nota: {menor_nota:.1f}")
    print("=" * 30)