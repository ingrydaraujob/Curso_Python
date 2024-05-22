cont = 0
valores = []
while True:
    num = int(input("digite um numero:"))
    if num not in valores:
        valores.append(num)
        cont = cont+ 1
    res=str(input("quer continuar? [S/N]")).upper().strip()[0]
    if res in "Nn":
        break
print("-=-"*15)
print("a quantidade de numeros digitados foram",cont)
valores.sort (reverse=True)
print("a ordem decrescente dos valores sao:", valores)
if 5 in valores:
    print("o numero 5 está na lista")
else:
    print("o numero 5 não está na lista ")

