import random 
numeros = []
def sorteio():
    for i in range(5):
        numero = random.randint(1,10)
        numeros.append(numero)

def somapar():
    soma = 0
    for numero in numeros:
        if numero % 2==0:
            soma += numero
    print(f"a soma dos numeros {numeros} pares é:{soma}")

sorteio()
somapar()