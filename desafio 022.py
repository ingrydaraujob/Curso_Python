num = int(input("dígite um numero com 4 dígitos:")) 

if num < 1000 or num > 9999:
    print("pfvr, digite um numero que tenha 4 dígitos")
else:
    milhar = num // 1000
    centena = (num % 1000) // 100
    dezena =  (num % 100) // 10
    unidade = num % 10 

print("milhar",milhar)
print("centena",centena)
print("dezena",dezena)
print("unidade",unidade)
