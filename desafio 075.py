palavra = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADORA", "FUTURO", "TRISTEZA")
for vog in palavra:
    print(f"\nna palavra {vog.upper()} temos:", end="")
    for letra in vog:
        if letra.lower() in "aeiou":
            print(letra , end=" ")
