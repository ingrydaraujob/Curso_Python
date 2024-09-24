import random
numeros = [] 
def sorteio():
    #print(f"sorteando 5 valores da lista {numeros}",end="")
    for i in range(5):
        numero = random.randint(1,10)
        numeros.append(numero)
        #print(f"{numeros}", end=" ",flush=True)

def somapar():
    soma = 0
    for valor in numeros:
        if valor % 2==0:
            soma += valor
    print(f"a soma dos numeros {numeros} pares é {soma}")


sorteio()  
somapar()