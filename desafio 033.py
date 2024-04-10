salario = float(input("digite o seu salario:"))

if salario >= 1250:
    aumento = salario * 10/100
    sal_novo = salario + aumento
elif salario < 1250:
    aumento = salario * 15/100
    sal_novo = salario + aumento

print(f"o seu salario é de {salario} reais, mas com o aumento fica {sal_novo} reais")