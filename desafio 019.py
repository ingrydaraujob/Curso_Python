import random
n1 = str(input("primeiro nome:"))
n2 = str(input("segundo nome:"))
n3 = str(input("terceiro nome:"))
n4 = str(input("quarto nome:"))
lista = [n1, n2,n3,n4]
escolhido = random.choice(lista)
print("O aluno escolhido para apagar o quadro é:", escolhido)
