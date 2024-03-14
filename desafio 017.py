import math
cateto_opo = float(input("digite o valor do cateto oposto:"))
cateto_adja = float(input("digite o valor do cateto adjacente:"))
hipotenusa = math.sqrt(cateto_opo **2 + cateto_adja ** 2 )
print("O comprimento da hipotenusa é:{:.2f}".format (hipotenusa))