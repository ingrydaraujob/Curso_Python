frase = input("digite uma frase:")

quant_a = frase.count("a") + frase.count("A")
primeira_posição = min(frase.find("a"), frase.find("A"))
ultima_posição = max(frase.rfind("a"), frase.rfind("A"))


print(f"na frase contém: {quant_a} 'a' ")
print(f"o primeiro 'a' esta na: {primeira_posição}")
print(f"o ultima 'a' esta na: {ultima_posição}")