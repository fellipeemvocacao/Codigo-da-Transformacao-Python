def salvar_dados(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"✅ Dados gravados com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"❌ Erro ao gravar: {e}")

def ler_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("\n--- Conteúdo Lido do Arquivo ---")
            print(conteudo)
            print("--------------------------------")
    except FileNotFoundError:
        print(f"⚠️ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"❌ Erro ao ler: {e}")
if __name__ == "__main__":
    nome_do_arquivo = "relatorio_vendas.txt"
    texto_para_salvar = "Relatório de Vendas - Maio 2026\n" + "-"*30 + "\nProduto: Notebook\nPreço: R$ 5.000,00\nStatus: Pago"

    salvar_dados(nome_do_arquivo, texto_para_salvar)

    ler_dados(nome_do_arquivo)