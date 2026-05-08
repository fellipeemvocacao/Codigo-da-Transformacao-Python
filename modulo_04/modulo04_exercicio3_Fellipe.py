def filtrar_pares_impares(numeros):
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
            
    return pares, impares

if __name__ == "__main__":
    import random
    conjunto_numeros = [random.randint(1, 100) for _ in range(10)]
    
    lista_pares, lista_impares = filtrar_pares_impares(conjunto_numeros)
    
    print(f"🔢 Conjunto Original: {conjunto_numeros}")
    print("-" * 40)
    print(f"✅ Pares: {lista_pares}")
    print(f"❌ Ímpares: {lista_impares}")