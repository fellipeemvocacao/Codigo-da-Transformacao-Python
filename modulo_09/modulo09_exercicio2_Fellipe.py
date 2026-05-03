class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = (f"Erro: Saldo insuficiente. "
                         f"Saldo disponível: R${saldo_atual:.2f}. "
                         f"Tentativa de saque: R${valor_saque:.2f}.")
        super().__init__(self.mensagem)
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${self.saldo:.2f}")
def executar_simulacao():
    minha_conta = ContaBancaria("Ivan", 1000.00)
    
    print(f"--- Bem-vindo ao Sistema Bancário ---")
    print(f"Cliente: {minha_conta.titular}")
    print(f"Saldo inicial: R${minha_conta.saldo:.2f}\n")

    transacoes = [250.00, 800.00, 100.00]

    for valor in transacoes:
        try:
            print(f"Tentando sacar: R${valor:.2f}...")
            minha_conta.sacar(valor)
            print("-" * 30)
        except SaldoInsuficienteError as erro:
            print(f"ALERTA: {erro}")
            print("-" * 30)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    print("\nFim da simulação.")
if __name__ == "__main__":
    executar_simulacao()