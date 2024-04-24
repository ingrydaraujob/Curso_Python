sexo = input("Digite o sexo (M/F): ").upper()
while sexo not in ['M', 'F']:
    sexo = input("Valor incorreto! Digite apenas M para masculino ou F para feminino: ").upper()

print("Sexo digitado corretamente:", sexo)

