ano = int(input("digite o ano do seu nascimento:"))

if ano > 2006:
    print("voce ainda vai se alistar")
elif ano == 2006:
    print("é a hora de se alistar:")
else:
    print("já passou do tempo de se alistar")