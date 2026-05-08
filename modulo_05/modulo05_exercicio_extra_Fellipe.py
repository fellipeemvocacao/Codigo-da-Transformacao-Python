def login_seguro():
    usuario_correto = "Ivan"
    senha_correta = "5119"
    
    print("--- ACESSO AO SISTEMA ---")
    while True:
        user = input("Usuário: ")
        password = input("Senha: ")
        
        if user == usuario_correto and password == senha_correta:
            print("Login realizado com sucesso!\n")
            return True
        else:
            print("Dados incorretos! Tente novamente.\n") 