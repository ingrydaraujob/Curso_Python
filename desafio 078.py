numeros = []
for i in range(0,5):
    num=int(input("digite um numero:"))
    if i==0 or num > numeros[-1]:
        numeros.append(num)
        print("adicionado no final da lista.")
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                print(f"adicionado na posição {pos} da lista.")
                break
            pos += 1 
print("-="*17)
print("os numeros digitados em ordem foram:",numeros)