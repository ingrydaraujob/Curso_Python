ano = int(input("digite o ano que voce nasceu:"))
ano1= 2025 - ano #trocar o 2025 pelo ano atual 
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



'''from datetime import date
atual = date.today().year
nascimento = int(input("digite o ano que voce nasceu:"))
idade = atual - nascimento
print(f"o atleta tem {idade} anos.")
if idade <= 9 :
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
else:
    print("MASTER")'''    