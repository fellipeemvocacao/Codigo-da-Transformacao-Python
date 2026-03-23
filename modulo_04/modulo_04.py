aluno = {
    "nome": "Pedro Silva",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5],
    "tarefas": []  
}

print(f"--- SISTEMA ESCOLAR: {aluno['nome'].upper()} ---")
media = sum(aluno['notas'])/len(aluno['notas'])
print(f"Idade: {aluno['idade']} anos | Média: {media:.1f}")

while True:
    aluno["tarefas"].sort()
    print(f"\n📋 Agenda de {aluno['nome']}: {aluno['tarefas']}")
    
    comando = input("Digite uma tarefa, 'remover', 'analisar números' ou 'sair': ").strip().lower()
    
    if comando == 'sair':
        break
        
    elif comando == 'remover':
        if len(aluno["tarefas"]) > 0:
            item_para_remover = input("Qual tarefa deseja remover? ")
            if item_para_remover in aluno["tarefas"]:
                aluno["tarefas"].remove(item_para_remover)
                print(f"🗑️ '{item_para_remover}' removida!")
            else:
                print(f"❌ Erro: '{item_para_remover}' não encontrada.")
        else:
            print("⚠️ A agenda já está vazia.")

    
    elif comando == 'analisar números':
        print("\n--- ANALISADOR DE PAR OU ÍMPAR ---")
        
        numeros = [10, 15, 22, 33, 40, 57, 68]
        pares = []
        impares = []

        for num in numeros:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        
        print(f"Números analisados: {numeros}")
        print(f"🔵 Pares: {pares}")
        print(f"🔴 Ímpares: {impares}")
            
    elif comando != "":
        aluno["tarefas"].append(comando)
        print(f"✅ '{comando}' adicionada ao perfil de {aluno['nome']}!")
    else:
        print("⚠️ Você não digitou nada.")