from random import randint
from time import sleep
computador = randint(0, 10) #esse comando faz o computador sortear os numeros qur colocamos 
print("-=- " * 13)
print("vou pensar em um número entre 0 e 10. tente adivinhar...")
print("-=- " * 13)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("em que numero eu pensei?"))
    palpites += 1
    print("processando...")
    sleep(0.5)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("mais... tente mais uma vez")
        elif jogador > computador:
            print("menos... tente mais uma vez.")
print(f"Acertou com {palpites} tentativas, PARABÉNS!!, voce venceu")
    