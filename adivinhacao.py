import random
secretNumber = random.randint(1,20)
print("Estou pensando em um número de 1 a 20")

for tentativas in range(1, 7):
    print("Tente adivinhar o número")
    guess = int(input())

    if guess < secretNumber:
        print("Sua tentativa foi muito baixa")
    elif guess > secretNumber:
        print("Sua tentativa foi muito alta")
    else:
        break

if guess == secretNumber:
    print("Parabéns! Você acertou o número em " + str(tentativas) + "tentativas")
else:
    print("Que pena! Você não conseguiu adivinhar o número que era: " + str(secretNumber))