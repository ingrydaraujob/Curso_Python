print("gerador de PA")
print("=-="*7)
primeiro = int(input("primeiro termo:"))
razão = int(input("razão:"))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo}  ", end="")
    termo += razão
    cont += 1
print("FIM")