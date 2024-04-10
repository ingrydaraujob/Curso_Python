velocidade = int(input("digite a velocidade de do carro:"))


if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print("voce foi multado")
    print("voce vai pagar uma multa de:", multa)
else:
    print("velocidade normal")