reta1 = float(input("digite o comprimento da reta1: "))
reta2 = float(input("digite o comprimento da reta2: "))
reta3 =float(input("digite o comprimento da reta3: "))

if reta1 == reta2 == reta3:
    print("pode formar um triangulo equilátero")
elif reta1 != reta2 != reta3:
    print("pode formar um triangulo escaleno")
else:
    print("triangulo isóceles")