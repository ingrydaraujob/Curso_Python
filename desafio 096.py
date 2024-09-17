def maior(*num):
    print("-="*20)
    cont = maior = 0
    print("\n analisando os valores passados...")
    for valor in num:
        print(f"{valor}", end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"foram informados {cont} valores ao todo.")
    print(f"o maior valor informado foi {maior}.")
maior(2,9,8,5,7,4)
maior(4,5,9,2)
maior(1,5,4)
maior(5,7)
maior(2)
maior()