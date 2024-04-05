frase =str(input("digite uma frase:")).upper().strip() 

print("A letra A aparece {} vezes".format(frase.count("A")))
print("o primeiro letra A apareceu posição {}" .format(frase.find("A")+1))
print("o ultima letra A apareceu na posição {}" .format(frase.rfind("A")+1))