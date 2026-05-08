# main.py
from interface.formatacao import exibir_titulo, formatar_moeda
from core.calculos import aplicar_desconto, calcular_icms
from core.validacoes import validar_produto

def processar_venda():
    exibir_titulo("Sistema de Vendas v2.0")
    
    produto = "Notebook Gamer"
    preco_base = 5000.00
    
    if validar_produto(produto):
        preco_final = aplicar_desconto(preco_base, 10)
        imposto = calcular_icms(preco_final)
        
        print(f"Produto: {produto}")
        print(f"Preço com Desconto (10%): {formatar_moeda(preco_final)}")
        print(f"Imposto Estimado: {formatar_moeda(imposto)}")
        print(f"Total: {formatar_moeda(preco_final + imposto)}")
    else:
        print("Erro: Produto inválido.")

if __name__ == "__main__":
    processar_venda()