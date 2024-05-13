extenso = ("zero", "um","dois", "tres", "quatro","cinco" , "seis" , "sete", "oito", "nove" , "dez" , "onze" , "doze","treze", "quartoze","quinze", "desesseis" , "desessete" , "dezoito","dezenove", "vinte")
while True:
    num = int(input("digite um numero de 0 ate 20:"))
    if 0 <= num <= 20:
        print(f"o numero {num} por extenso é {extenso[num]}")
    else:
        print(f"numero inválido. tente um numero entre 0 e 20:")

    continuar = input('Deseja continuar? (s/n) ').lower()
    if continuar != 's':
        print("FIM DO PROGRAMA")
        break