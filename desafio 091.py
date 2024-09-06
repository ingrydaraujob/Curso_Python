galera = list()
pessoa = dict()
while True:
    pessoa["nome"] = str(input("Nome:"))
    while True:
        pessoa["sexo"] = str(input("sexo[M/F]:")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! pfvr, digite apenas M ou F")
    pessoa["idade"]= int(input("Idade:"))
    while True:
        resp = str(input("quer continuar[S/N]:")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! responda apenas S ou N ")
    if resp == "S":
        break