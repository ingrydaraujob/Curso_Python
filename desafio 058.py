from math import factorial
num = int(input("digite um numero para calcular o seu fatorial:"))
fatorial = factorial(num)
print(f"o fatorial de {num} é {fatorial}") #simples

"""num = int(input("digite um numero para calcular o seu fatorial:"))
c = num
f = 1
while c > 0:
    print(c , end='')
    print("x" if c > 1 else "=",end="")
    f *= c
    c-=1  
print(f)"""
