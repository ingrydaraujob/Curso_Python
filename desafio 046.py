s = 0
cont = 0 
for c in range(1 , 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print("a soma dos multiplos de 3 é:",s)
print("a soma de todos os valores solicidados foram:",cont)