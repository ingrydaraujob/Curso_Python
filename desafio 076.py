numeros = []
for i in range (0,5):
    num = int(input("digite um numero:"))
    numeros.append(num)
    
maior = max(numeros)
menor = min(numeros)
posiçaomaiaor = numeros.index(maior)
posiçaomenor = numeros.index(menor)
print(f"o maior valor é {maior}, e sua posição é {posiçaomaiaor + 1}")
print(f"o menor valor é {menor}, e a sua posição é {posiçaomenor+1}")

    