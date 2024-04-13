from datetime import date
atual = date.today().year
nascimento = int(input("digite o ano do seu nascimento:"))
idade = atual - nascimento
print(f"quem nasceu em {nascimento} tem {idade} anos em {atual}")
if idade == 18:
    print("voce tem que se alistar IMEDIATAMENTE")
elif idade < 18:
    saldo = 18 - idade
    print(f"ainda faltam {saldo} anos para o alistamento")
    ano = atual + saldo
    print("seu alistamento será em:",ano)
elif idade > 18:
    saldo = idade - 18
    print(f"voce deveria ter se alistado há {saldo} anos")   
    ano = atual - saldo
    print("seu alistamento foi em:",ano)