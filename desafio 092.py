time = list()
dict = {}
list = []
while True:
    dict.clear()
    dict["jogador"] = str(input("Nome do jogador:"))
    partidas = int(input(f"quantas partidas {dict['jogador']} jogou?"))
    list.clear()
    for c in range(0,partidas):
        list.append(int(input(f"quantos gols na partida {c+1}?")))
    dict["gols"] = list[:]
    dict["total"] = sum(list)
    time.append(dict.copy())
    while True:
        resp = str(input("quer continuar? [S/N]")).upper().strip()[0]
        if resp in "SN":
           break
        print("ERRO! apenas S ou N.") 
    if resp == "N":
        break 
print("-="*20)
print("cod",end="")
for i in dict.keys():
    print(f"{i:<15} " , end="")
print()
print("-="*20)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}",end="")
    print()
print("-="*20)
while True:
    busca = int(input("mostrar dados de qual jogador?(999 para parar)"))
    if busca == 999:
        break
    if  busca >= len(time):
        print(f"ERRO! nao existe jogador com codigo {busca}")
    else:
        print(f" levantamento do jogador {time[busca]["jogador"]}:")
        for i, g in enumerate(time[busca] ["gols"]):
            print(f"no jogo {i + 1} fez {g} gols")
    print("-="*20)
print("VOLTE SEMPRE!")
