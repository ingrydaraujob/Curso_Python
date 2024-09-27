def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("por favor, digite um numero inteiro válido.")
        else:
            return n

num = leiaint("digite um numero:")
print(f"voce acabou de digitar o numero {num}")