reta1 = float(input("digite o comprimento da reta1:"))
reta2 = float(input("digite o comprimento da reta2:"))
reta3 = float(input("digite o comprimento da reta3:"))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("podem formar um triangulo")
    if reta1 == reta2 == reta3:
        print("pode formar um triangulo equilátero")
    elif reta1 != reta2 != reta3:
        print("pode formar um triangulo escaleno")
    else:
        print("pode forma um triangulo isóceles") 

else:
    ("não podem formar um triangulo")

 