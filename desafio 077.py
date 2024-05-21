numeros = []
while True:
    num = int(input("digite um numero:"))
    if num not in numeros:
        numeros.append(num)
        print("valores cadastrados com sucesso:")
    else:
        print("valor duplicado! nao será adicionado.")
    res=str(input("quer continuar? [S/N]")).upper().strip()[0]
    if res in "Nn":
        break
print("-=-"*17)
print("voce digitou os numeros:",sorted(numeros))