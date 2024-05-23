temp = []
principal = []
maior = menor = 0
while True:
    temp.append(str(input("Nome:")))
    temp.append(float(input("peso:")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp=str(input("quer continuar?[S/n]")).upper().strip()[0]
    if resp in "Nn":
        break
print("-="*22)
print(f"ao todo voce cadastou {len(principal)} pessoas")
print(f"o maior peso foi de {maior}kg  peso de",end="") 
for p in principal:
    if p[1]==maior:
        print(f"[{p[0]}]",end="")
print(f"o menor peso foi de {menor}kg peso de ",end="")
for p in principal:
    if p[1] == menor:
        print(f"[{p[0]}]",end="")
print()