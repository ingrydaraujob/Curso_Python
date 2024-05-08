cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
saque = int(input("digite o valor a ser sacado:"))
while saque > 0:
    if saque >= 50:
        cedulas50 = cedulas50 + 1
        saque = saque - 50
    elif saque >= 20:
        cedulas20 = cedulas20 + 1 
        saque = saque - 20
    elif saque >= 10:
        cedulas10 = cedulas10 + 1 
        saque = saque - 10
    elif saque >= 1:
        cedulas1 = cedulas1 + 1 
        saque = saque - 1 
print(f"total de cédulas de R$50: {cedulas50}")
print(f"total de cédulas de R$20: {cedulas20}")
print(f"total de cédulas de R$10: {cedulas10}")
print(f"total de cédulas de R$1: {cedulas1}")