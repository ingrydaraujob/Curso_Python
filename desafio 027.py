from random import randint
from time import sleep
computador = randint(0, 5) #esse comando faz o computador sortear os numeros qur colocamos 
print("-=- " * 13)
print("vou pensar em um número entre 0 e 5. tente adivinhar...")
print("-=- " * 13)
jogador = int(input("em que numero eu pensei?"))
print("processando...")
sleep(0.5)
if jogador == computador:
    print("PARABÉNS!!, voce venceu")
else:
    print(f"GANHEI!!! eu pensei em {computador} e não em {jogador} ")