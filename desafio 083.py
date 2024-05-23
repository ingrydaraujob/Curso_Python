numeros = []
pares = []
impares = []
for p in range(0,7):
    num = int(input("digite um numero:"))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num) 
    else:
        impares.append(num)
impares.sort()
pares.sort()
print(f"valores impares: {impares}")
print(f"valores pares: {pares}" )