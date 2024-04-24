from time import sleep 
num1 = float(input("digite o primeiro valor:"))
num2 = float(input("digite o segundo valor:"))
condição = 0
while condição != 5:
    print('''
      [1] Somar
      [2] Multiplicar 
      [3] Maior entre eles 
      [4] Novos números 
      [5] Sair do programa''')
    condição = int(input(">>>>> Qual a sua opção: "))
    if condição == 1:
        soma = num1 + num2
        print("a soma dos valores solicitados é",soma)
    elif condição == 2:
        multi = num1 * num2
        print("a multiplicação dos valores solicitados é de:",multi)
    elif condição == 3:
        maior = max(num1,num2)
        print("o maior valor solicitado é:",maior)
        if num1 == num2:
            print("os numeros são iguais ")
    elif condição == 4:
        num1 = int(input("digite o novo valor:"))
        num2 = int(input("digite um novo valor:"))
    elif condição == 5:
        print("Finalizando...")
    else:
        print("opção inválida. tente novamente")
    print("=-="*7)
    sleep(1)
print("Fim do programa!!")