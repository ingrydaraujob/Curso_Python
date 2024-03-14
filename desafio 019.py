import random
alunos = []
for i in range(4):
    nome_aluno = input("Digite o nome do aluno {}: ".format(i+1))
    alunos.append(nome_aluno)

escolhido = random.choice(alunos)

print("O aluno escolhido para apagar o quadro é:", escolhido)
