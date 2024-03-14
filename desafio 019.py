import random
alunos = []
for i in range(4):
    nome = input("digite o nome do aluno{}:".format(i+1))
    alunos.append(nome)
escolhido = random.choice(alunos)
print("o aluno escolhido para apagar o quadro é:",escolhido)