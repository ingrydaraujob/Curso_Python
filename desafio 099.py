def fatorial(num, show=False):
    f = 1
    for i in range(1, num + 1):
        f *= i
        if show:
            print(f'{i}! = {f}')
    return f

num = int(input('Digite um número: '))
mostrar = input('Deseja mostrar o cálculo? (S/N) ').upper() == 'S'
resultado = fatorial(num, mostrar)
print(f'O fatorial de {num} é {resultado}')