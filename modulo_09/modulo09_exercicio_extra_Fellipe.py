class CredenciaisInvalidasError(Exception):
    pass

class AcessoBloqueadoError(Exception):
    pass

class SistemaLogin:
    def __init__(self):
        self._usuarios_cadastrados = {
            "admin": "1234",
            "guilherme": "python321",
            "ana": "senhaSegura"
        }
        self.tentativas_maximas = 3
    def autenticar(self):
        tentativas = 0
        print("--- Sistema de Login ---")
        while tentativas < self.tentativas_maximas:
            try:
                usuario = input("\nUsuário: ").strip()
                senha = input("Senha: ").strip()
                if not usuario or not senha:
                    print("Erro: Usuário e senha não podem estar vazios.")
                    continue
                if usuario in self._usuarios_cadastrados and self._usuarios_cadastrados[usuario] == senha:
                    print(f"\n✅ Login bem-sucedido! Bem-vindo, {usuario}.")
                    return True
                else:
                    tentativas += 1
                    restantes = self.tentativas_maximas - tentativas
                    raise CredenciaisInvalidasError(f"Credenciais incorretas. Tentativas restantes: {restantes}")

            except CredenciaisInvalidasError as e:
                print(f"❌ {e}")
        raise AcessoBloqueadoError("Conta bloqueada após 3 tentativas malsucedidas. Contate o administrador.")

sistema = SistemaLogin()

try:
    sistema.autenticar()
except AcessoBloqueadoError as erro:
    print(f"\n⚠️ SEGURANÇA: {erro}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("\nSessão encerrada.")