""""dict = {}
dict["nome"] = str(input("nome do jogador:"))
dict["partidas"] = int(input("partidas jogadas:"))
dict[" total de gols"] = int(input("total de gols:"))
dict["media de gols"] = dict[" total de gols"] / dict["partidas"]
for k, v in dict.items():
    print(f" - {k} tem valor {v}")
#print(dict)"""
totgols = 0
dict = {}
dict["nome"] = str(input("nome do jogador:"))
dict["partidas"] = int(input(f"quantas partidas {dict['nome']} jogou?"))
for i in range(0,dict["partidas"]):
    dict["gols"] = int(input(f"quantos gols na partida {i} ?"))
    totgols += 1
for k , v in dict.items():
    print(f"- {k}")