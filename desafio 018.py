import math
angulo = float(input("Digite o valor do angulo:"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno do angulo é:{:.2f}".format(seno))
print("o cosseno é:{:.2f}".format(cosseno))
print(" a tangente é:{:.2f}".format(tangente)) 