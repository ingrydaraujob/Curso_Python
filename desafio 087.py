ficha = []
while True:
    nome = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input("quer continuar [S/N]")).upper() .strip()[0]
    if resp in "Nn":
        break
print("=-"*24)
print(f"{"No.": <4}{"NOME":<10}{"MÉDIA":>8}")
print("=-"*24)
for i , a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:<8.1f}")
while True:
    print("-="*24)
    opc = int(input("mostrar notas de qual aluno?(999 interrompe):"))
    if opc == 999:
        print("finalizando...")
        break
    if opc<=len(ficha) - 1:
        print(f"notas de {ficha[opc][0]} sao {ficha[opc][1]}")
print("volte sempre")