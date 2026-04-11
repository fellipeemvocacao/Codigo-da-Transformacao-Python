import random
import math

def jogar():
    print("\n" + "="*36)
    print("\n   BEM-VINDO AO DESAFIO MATEMÁTICO!   ")
    print("\n" + "="*36)
    print("\nQual número, entre 1 e 100, eu escolhi?")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            chute = int(input("\nQual o seu palpite? "))
            tentativas += 1
            distancia = math.fabs(numero_secreto - chute)

            if chute == numero_secreto:
                print(f"🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
                acertou = True
            elif chute < numero_secreto:
                print("DICA: Mais alto! ↑")
            else:
                print("DICA: Mais baixo! ↓")

            # Feedback extra usando math para proximidade
            if not acertou:
                if distancia <= 5:
                    print("🔥 VOCÊ ESTÁ FERVENTE! Muito perto!")
                elif distancia <= 15:
                    print("暖 OPA! Está ficando quente...")
                else:
                    print("❄️ Frio... ainda está longe.")

        except ValueError:
            print("❌ Por favor, digite apenas números inteiros!")

    print("\nObrigado por jogar!")

if __name__ == "__main__":
    jogar()