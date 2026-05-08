from utilidades import somar, subtrair, calcular_potencia

def executar_programa():
    print("--- Calculadora via Módulo Externo ---")
    n1, n2 = 15.5, 10.5
    resultado_soma = somar(n1, n2)
    print(f"Soma: {n1} + {n2} = {resultado_soma}")

    resultado_sub = subtrair(100, 45)
    print(f"Subtração: 100 - 45 = {resultado_sub}")

    base, exp = 2, 10
    resultado_pot = calcular_potencia(base, exp)
    print(f"Potência: {base} elevado a {exp} = {resultado_pot}")

if __name__ == "__main__":
    executar_programa()