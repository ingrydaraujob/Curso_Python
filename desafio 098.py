import datetime
def eleição():
    ano = datetime.date.today().year
    nas = ano - nascimento
    if  nas < 16:
        return (f" com {nas} anos: VOTO NEGADO.")
    elif 16 <= nas < 18 or nas > 65:
        return (f"com {nas} anos: VOTO OPCIONAL.")
    else :
        return (f"com {nas} anos: VOTO OBRIGATÓRIO.")
    print(f"voce tem {nas} : ",end=" " )



nascimento = int(input("Em que ano você nasceu?"))
print(eleição())
    