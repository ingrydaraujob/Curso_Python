import time 
def contagem(i, f, p):
    print("-="*10)
    print(f"contagem de {i} até {f} de {p} em {p}")
    print("-="*10)
    time.sleep(2)
    if p < 0:
        p *= -1
        while i >= f:
            print(f"{i}", end=" ", flush=True)
            time.sleep(0.5)
            i -= p
    else:
        while i <= f:
            print(f"{i}", end=" ", flush=True)
            time.sleep(0.5)
            i+= p        
    print()

contagem(1,10,1)
contagem(10,0,2)
print("agora é sua vez de prsonalizar a contagem!")
inicio = int(input("inicio:"))
fim = int(input("fim:"))
passo = int(input("passo:"))
contagem(inicio, fim, passo)