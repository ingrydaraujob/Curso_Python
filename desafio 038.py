ano = int(input("digite o ano do seu nascimento:"))

if ano > 2006:
    tempo = 2024 - ano 
    tempo1 = 18 - tempo
    print("voce ainda vai se alistar")
    print(f"faltam {tempo1} ano(s) para o alistamento")
elif ano == 2006:
    print("é a hora de se alistar:")
else:
    tempo = 2024 - ano - 18
    print("já passou do tempo de se alistar")
    print("ja se passaram",tempo)
    