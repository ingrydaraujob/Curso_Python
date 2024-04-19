pesos = []
for c in range(1,6):
    peso = float(input("digite o peso  da {} pessoa:".format(c)))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
print(f"o menor peso é {menor} e o maior peso é {maior} ")