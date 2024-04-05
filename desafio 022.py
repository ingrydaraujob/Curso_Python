num = int(input("dígite um numero com 4 dígitos:")) 
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10  

print("milhar",milhar)
print("centena",centena)
print("dezena",dezena)
print("unidade",unidade)
