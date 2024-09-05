dict = {}
list = []
dict["jogador"] = str(input("Nome do jogador:"))
partidas = int(input(f"quantas partidas {dict['jogador']} jogou?"))
for c in range(0,partidas):
    list.append(int(input(f"quantos gols na partida {c}?")))
dict["gols"] = list[:]
dict["total"] = sum(list)
print("-="*20)
print(dict)
print("-="*20)
for k, v in dict.items():
    print(f"o campo {k} tem o valor {v}")
print("-="*20)
print(f"o jogador{dict['jogador']} jogou {len(dict['gols'])} partidas ")
for i , v in enumerate(dict["gols"]):
    print(f"na partida {i}, fez {v} gols")
print(f"foi um total de {dict["total"]} gols")