list = []
while True:
    aluno = float(input("nota do aluno:"))
    list.append(aluno)
    resp = str(input("quer continuar?S/N")).strip().upper()
    if resp == "N":
        break


quantidade = len(list)
maior = max(list)
menor = min(list)
media = sum(list)/ len(list)
print(f"a quantidade de notas adicionadas foram {quantidade}")
print(f"a maior nota foi {maior}, e a menor foi {menor}")       
if media < 5:
    print(f"a media {media} ta pessima")
elif media < 7:
    print(f"a media {media} ta razoavel")
else:
    print(f"{media} muito boa")