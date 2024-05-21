numeros = []
while True:
    num = int(input("digite um numero [ou 000 para parar]:"))
    if num == 000:
        break
    if num not in numeros:
        numeros.append(num)
        print("valores cadastrados com sucesso:")
    else:
        print("valor duplicado! nao será adicionado.")

print("-=-"*17)
print("voce digitou os numeros:",sorted(numeros))