valores = (int(input("digite o primeiro valor:")),
           int(input("digite o segundo valor:")),
           int(input("digite o terceiro valor:")),
           int(input("digite o quarto valor:")))
cont = valores.count(9)
print(f"o numero 9 apareceu {cont} vezes.")

if 3 in valores:
    posiçao = valores.index(3)
    print(f"o numero 3 estar na posição {posiçao+1}")
else:
    print("o valor 3 nao foi digitado em nenhuma posição")

for num in valores:
    if num % 2 ==0:
        print(f"os numeros pares digitados foram: {num}")