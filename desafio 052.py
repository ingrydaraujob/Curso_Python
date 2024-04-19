from datetime import date
atual = date.today().year
maior = 0
menor = 0 
for pess in range(1,8):  
    ano = int(input("em que ano {} pessoa nasceu?".format(pess)))
    idade = atual - ano
    if idade >= 21:
        maior = maior+1
    else:
        menor = menor+1
print(f"ao total tivemos {maior} pesssoas de maiores de idade ")
print(f"e tivemos {menor} pessoas menores de idade")
