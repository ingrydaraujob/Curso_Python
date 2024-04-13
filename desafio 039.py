nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
media = (nota1 + nota2)/2
print("sua media:",media)
if media < 5 :
    print("-=-"*6)
    print("REPROVADO")
    print("-=-"*6)
elif media == 5 or media <= 6.9:
    print("-=-"*6)
    print("RECUPERAÇÃO")
    print("-=-"*6)
else:
    print("-=-"*6)
    print("APROVADO")
    print("-=-"*6)