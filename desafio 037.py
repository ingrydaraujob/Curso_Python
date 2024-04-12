num1 = int(input("digite o primerio numero inteiro:"))
num2 = int(input("digite o segundo nuemro inteiro:"))
if num1 > num2:
    print(f"o primeiro valor {num1} é maior")
elif num2 > num1:
    print(f"o segundo  valor {num2} é maior")
else:
    print("não existe valor maior, os dois sao iguais")