class EntradaInvalidaError(Exception):
    pass

def validar_idade():
    while True:
        try:
            entrada = input("Digite sua idade: ")
            if not entrada.isdigit() and not (entrada.startswith('-') and entrada[1:].isdigit()):
                raise ValueError("A entrada deve ser um número inteiro.")
            
            idade = int(entrada)
            if idade < 0:
                raise EntradaInvalidaError(f"Idade inválida ({idade}). A idade não pode ser negativa.")
            if idade > 120:
                raise EntradaInvalidaError(f"Idade inválida ({idade}). Valor acima do limite humano esperado.")
            
            return idade
            
        except ValueError as e:
            print(f"Erro de Formato: {e}. Tente novamente.")
        except EntradaInvalidaError as e:
            print(f"Erro de Regra: {e}. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def validar_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if len(nome) < 3:
            print("Erro: O nome deve ter pelo menos 3 caracteres.")
            continue
        return nome
print("--- Cadastro de Usuário ---")
nome_usuario = validar_nome()
idade_usuario = validar_idade()

print("\n--- Cadastro Realizado ---")
print(f"Nome: {nome_usuario}")
print(f"Idade: {idade_usuario} anos")