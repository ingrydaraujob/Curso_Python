maiores = homens = menores  = 0
print("=-="*13)
print("CADASTRAMENTO DE PESSOAS")
print("=-="*13)
while True:
    idade = int(input("digite a idade da pessoa:"))
    sexo = str(input("digite o sexo da pessoa:[M/F]")).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens +=1
    if sexo == "F" and idade < 20:
        menores += 1 
    continuar = str(input("voce quer continuar o cadastramento das pessoas? [S/N]:")).strip().upper()
    if continuar != "S":
        print("FIM DO PROGRAMA")
        break
print(f"A quantidade de pessoas com mais de 18 anos é de {maiores} pessoas")
print(f"A quantidade de homens cadastrados é de {homens}")
print(f"A quantidade de mulheres com menos de 20 anos é de {menores} ")