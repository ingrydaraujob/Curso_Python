aluno = {}
lista = []
aluno["nome"] = str(input("Nome:"))
aluno["media"] = float(input(f"média de {aluno['nome']}"))
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["media"] >= 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"
print("=-"*17)
for k , v in aluno.items():
    print(f" - {k} é igual a {v}")
