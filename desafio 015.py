dias = int(input("digite os dias que o carro foi alugado:"))
km = float(input("digite a quantidade de km rodados: "))
dias1 = dias * 60 
km1 = km * 0.15
total = dias1 + km1
print("o total a pagar é:",total)