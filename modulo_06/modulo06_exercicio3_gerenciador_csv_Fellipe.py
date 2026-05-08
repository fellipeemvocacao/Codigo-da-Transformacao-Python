import csv
import os

CAMINHO_CSV = "notas_alunos.csv"

def salvar_nota(nome, disciplina, nota):
    arquivo_existe = os.path.exists(CAMINHO_CSV)
    with open(CAMINHO_CSV, 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        
        if not arquivo_existe:
            escritor.writerow(["Nome", "Disciplina", "Nota"])
        
        escritor.writerow([nome, disciplina, nota])

def carregar_notas():
    notas = []
    if not os.path.exists(CAMINHO_CSV):
        return notas

    with open(CAMINHO_CSV, 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f) 
        for linha in leitor:
            notas.append(linha)
    return notas