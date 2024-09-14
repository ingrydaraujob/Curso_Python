def linha():
    print("-="*15)
linha()
print(" CONTROLE DE TERRENO ")
linha()
def area(l,c):
    area = l * c
    print(f"a area de um terreno {l}x{c} é de {area}m  ")

l = float(input("largura(m):"))
c = float(input("comprimento(m):"))
area(l,c)
