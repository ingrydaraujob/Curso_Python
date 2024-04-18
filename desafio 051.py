frase = str(input("digite uma frase:")).lower()
frase = frase.replace("","")

if frase == frase[::-1]:
    print("é um palíndromo")
else:
    print("nao é um polindromo")