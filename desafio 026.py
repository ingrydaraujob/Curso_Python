nome = input("digite seu nome completo:").strip()
n = nome.split()
primeira_posição = n[0]
ultima_posição = n[len(n)-1]

print(f"o primeiro nome: {primeira_posição}")
print(f"o ultima nome: {ultima_posição}")
