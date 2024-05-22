valores = []
par = []
impar = []
while True:
    num = int(input("digite um numero:"))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    res = str(input("quer continuar? [S/N]")).upper().strip() [0]
    if res in "Nn":
        break

print("-="*17)
print("lista completa:",valores)
print("lista dos numeros pares:",par)
print("lista dos nuemros impares:",impar)