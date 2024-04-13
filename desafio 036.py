num = int(input("digite um numero inteiro:"))
print('''escolha umas das bases para a conversão
      [1] converter para BINÁRIO
      [2] converter para octal
      [3] converter para hexadecimal''')
opção = int(input("sua opção:"))

if opção == 1:
    print("convertido para binário:",bin(num))
elif opção == 2:
    print("convertido para octal:" ,oct(num))
elif opção == 3:
    print("convertido para hexadecimal:", hex(num))
