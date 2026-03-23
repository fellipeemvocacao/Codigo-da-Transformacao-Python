nome_aluno = input("Digite seu nome: ")
print(f"Olá, {nome_aluno}!")

nota1_aluno = float(input("Digite sua nota do 1° Bimestre: "))
nota2_aluno = float(input("Digite sua nota do 2° Bimestre: "))
nota3_aluno = float(input("Digite sua nota do 3° Bimestre: "))
nota4_aluno = float(input("Digite sua nota do 4° Bimestre: "))

def calcula_media(nota1, nota2, nota3, nota4):
  media = (nota1 + nota2 + nota3 + nota4) / 4
  if media >= 7:
   return media, "Aprovado"
  else:
   return media, "Reprovado"
  
resultado, status = calcula_media(nota1_aluno, nota2_aluno, nota3_aluno, nota4_aluno)
print("=" * 30)
print(f"Aluno: {nome_aluno}")
print(f"Média Final: {resultado:.1f}") 
print(f"Status: {status}")
print("=" * 30)