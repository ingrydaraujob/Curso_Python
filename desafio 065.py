while True:
    numero = int(input("digite o valor que quer para a tabuada:"))
    if numero < 0:
        print("programa encerrado.")
        break
    print("-=-"*10)
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
      
