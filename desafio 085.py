matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"digite um valor [{l}],[{c}]: "))
print("-=-"*17)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz [l] [c]:^5}]",end="")
        if matriz [l][c] % 2 == 0:
            spar+= matriz[l][c]
    print()

print("=-="*18)
print(f"a soma dos pares sao:{spar}")
for l in range(0,3):
    scol += matriz[l][2]
print(f"a soma dos valores da terceira coluna é {scol}")
for c in range (0,3):
    mai = max(matriz[1])
print(f"o maior valor da segunda linha é: {mai}")
