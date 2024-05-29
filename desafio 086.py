print("-"*30)
print("JOGO DA MEGA DA VIRADA")
print("-"*30)
import random
numjogos = int(input("quantos jogos voce quer gerar?"))
jogos = []
for i in range(numjogos):
    jogo = random.sample(range(1,61),6)
    jogos.append(jogo)
print("os jogos gerados sao:")
for i,jogo in enumerate(jogos,1):
    print(f"jogo {i}: {sorted(jogo)}")