matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"digite um valor {l},{c}: "))
print("-=-"*17)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz [l] [c]:^5}]",end="")
    print()