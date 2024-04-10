distancia = int(input("digite a distancia da viagem percorrida em km:"))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f"o valor da passagem é de: {passagem} reias")
elif distancia > 200:
    passagem2 = distancia * 0.45
    print(f"o valor da sua passagem é de: {passagem2} reais")