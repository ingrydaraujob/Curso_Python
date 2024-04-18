num = int(input("digite um numero inteiro:"))
total  = 0 
for c in range (1, num + 1):
    if num % c == 0 :
        print("\033[33m")
        total = total + 1
    else:
        print("\033[31m")
    print(c)
print(f"o numero {num} foi divisivel {total} vezes ")
if total == 2:
    print("é por isso que ele é PRIMO")
else:
    print("e por isso ele nao é primo ")