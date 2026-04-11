from dados.gerenciador_json import salvar_arquivo
from processamento.calculos import aplicar_desconto

def executar():
    print("--- Sistema de Vendas Inicializado ---")
    
    venda = {"item": "Notebook", "preco": 5000}
    preco_final = aplicar_desconto(venda['preco'], 10)
    
    venda['preco_final'] = preco_final
    salvar_arquivo("venda_final.json", venda)
    
    print(f"Venda processada: R$ {preco_final}")

if __name__ == "__main__":
    executar()