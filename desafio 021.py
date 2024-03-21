nome = input("Digite seu nome completo: ")
nomemaiusculo = nome.upper()
nomeminusculo = nome.lower()

letrastotal = len(nome.replace(" ", ""))

partes_nome = nome.split()

primeiro_nome = partes_nome[0]

num_letras_primeiro_nome = len(primeiro_nome)

print("Nome em maiúsculas:", nomemaiusculo)
print("Nome em minúsculas:", nomeminusculo)
print("Total de letras (sem espaços):", letrastotal)
print("Letras no primeiro nome:", num_letras_primeiro_nome)


