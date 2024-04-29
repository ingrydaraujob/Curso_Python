print("gerador de PA")
print("=-="*7)
primeiro = int(input("primeiro termo:"))
razão = int(input("razão:"))
termo = primeiro
cont = 1
total = 0
mais = 10 
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo}  ", end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais =int(input("quantos termos voce quer mostrar a mais?"))
print(f"Progressao finalizada com {total} termos mostrado. ")