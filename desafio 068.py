print("-"*15)
print("LOJA BARATÃO")
print("-"*15)
gastos = mil = menor= cont= 0
barato = " "
while True:
    produto = str(input("Nome do produto:"))
    preço = float(input("preço do produto:"))
    gastos = gastos + preço
    cont = cont + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if preço >= 1000:
        mil += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar != "S":
        print("FIM DO PREOGRAMA")
        break

print(f"o total da compra foi de {gastos}")
print(f"temos {mil} produtos custando mais de 1000 reais")
print(f"o produto mais barato foi {barato} que custa {menor} ")