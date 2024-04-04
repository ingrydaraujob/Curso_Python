nome = input("digite seu nome completo:")

primeira_posição = min(nome.find())
ultima_posição = max(nome.rfind())

print(f"o primeiro nome: {primeira_posição}")
print(f"o ultima nome: {ultima_posição}")
