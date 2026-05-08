from banco_dados.gerenciador_json import salvar_clientes, carregar_clientes

def executar():
    clientes_novos = {
        "1": {"nome": "Ana Souza", "email": "ana@email.com", "pontos": 150},
        "2": {"nome": "Bruno Lima", "email": "bruno@email.com", "pontos": 80}
    }

    if salvar_clientes(clientes_novos):
        print("💾 Dicionário de clientes salvo com sucesso em JSON!")

    dados_carregados = carregar_clientes()
    
    print("\n--- Clientes Carregados do JSON ---")
    for id_cliente, info in dados_carregados.items():
        print(f"ID: {id_cliente} | Nome: {info['nome']} | E-mail: {info['email']}")

if __name__ == "__main__":
    executar()