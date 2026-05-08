def maior_menor(numeros):
    if not numeros:
        return None, None
    
    maior = max(numeros)
    menor = min(numeros)
    
    return maior, menor

if __name__ == "__main__":
    lista_exemplo = [15, 42, 3, 89, 21, 55, 1, 67]
    v_maior, v_menor = maior_menor(lista_exemplo)
    
    print(f"Lista: {lista_exemplo}")
    print(f"Maior valor: {v_maior}")
    print(f"Menor valor: {v_menor}")