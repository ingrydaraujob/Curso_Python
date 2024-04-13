peso = float(input("digite o seu peso:"))
altura = float(input("digite a sua altura:"))
imc = peso / altura**2
print("seu imc é de:",imc)
if imc <= 18.5:
    print("-=-"*6)
    print("ABAIXO DO PESO")
    print("-=-"*6)
elif imc <= 25:
    print("-=-"*6)
    print("PESO IDEAL")
    print("-=-"*6)
elif imc <= 30:
    print("-=-"*6)
    print("SOBREPESO")
    print("-=-"*6)
elif imc <= 40:
    print("-=-"*6)
    print("OBESIDADE")
    print("-=-"*6)
else:
    print("-=-"*6)
    print("OBESIDADE MORBIDA")
    print("-=-"*6)
