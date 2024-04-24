sexo = str(input("informe seu sexo [m/f]:")).strip() .upper()[0]
while sexo not in "mMFf":
    s = str(input("dados invalidos. pfvr, informe seu sexo:")).strip() .upper()[0]
print("sexo resgistrado com sucesso:",sexo)
