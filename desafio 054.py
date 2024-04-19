somaidade = 0 
mediaidade = 0 
maioridadehomem = 0 
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print("------- {} PESSOA -------".format(c))
    nome = str(input("NOME:")).strip()
    idade = int(input("IDADE:"))
    sexo = str(input("SEXO:[M/F]")).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print(f"a media de idade do grupo é de {mediaidade} ")
print(f"o homem mais velho tem {maioridadehomem} anos e se chama {nomevelho} ")
print(f"ao todo sao {totmulher20} mulheres com menos de 20 anos")