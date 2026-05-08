def exibir_titulo(texto):
    print("\n" + "=" * 30)
    print(f"{texto.upper():^30}")
    print("=" * 30)

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}"