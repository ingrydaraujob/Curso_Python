ano = int(input("digite o ano que voce nasceu:"))
ano1= 2024 - ano
print(f"voce tem {ano1} anos")
if ano1 <= 9 :
    print("MIRIM")
elif ano1 <= 14:
    print("INFANTIL")
elif ano1 <= 19:
    print("JUNIOR")
elif ano1 <= 20:
    print("SENIOR")
else:
    print("MASTER")