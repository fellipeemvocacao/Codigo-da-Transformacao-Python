aluno = {
    "nome": "Fellipe Barros",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5],
    "tarefas": []  
}

print(f"--- SISTEMA ESCOLAR: {aluno['nome'].upper()} ---")
media = sum(aluno['notas'])/len(aluno['notas'])
print(f"Idade: {aluno['idade']} anos | Média: {media:.1f}")