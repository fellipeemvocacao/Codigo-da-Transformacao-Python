def saudacao(nome):
    mensagem = f"Olá, {nome}! Seja bem-vindo ao sistema."
    print(mensagem)

if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ")
    saudacao(nome_usuario)