casa = float(input("digite o valor da casa:"))
salario = float(input("digite o seu salario:"))
anos = int(input("digite em quantos anos de financiamento:"))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print("a prestação vai ser de:" , prestação)
print("minino:",minimo)
if prestação <= minimo:
    print("-=-"*6)
    print("emprestimo pode ser CONCEDIDO")
    print("-=-"*6)
else:
    print("-=-"*6)
    print("emprestimo NEGADO")
    print("-=-"*6)
 