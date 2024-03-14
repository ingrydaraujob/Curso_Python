import random

# Lista para armazenar os nomes dos alunos
alunos = []

# Loop para ler os nomes dos alunos
for i in range(4):
    nome_aluno = input("Digite o nome do aluno {}: ".format(i+1))
    alunos.append(nome_aluno)

# Embaralhando a ordem dos alunos
random.shuffle(alunos)

# Exibindo a ordem sorteada de apresentação dos trabalhos
print("Ordem sorteada de apresentação dos trabalhos:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")