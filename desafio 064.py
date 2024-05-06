num = soma = cont = 0
while True:
    num = int(input("digite um numero inteiro:(e 999 para parar)"))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f"a soma dos numeros inteiros foi de {soma} e foram necessarios {cont} numeros para obter esse valor")
