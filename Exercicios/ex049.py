print('Tabuada v2.0\n')

n = int(input('Digite um número: '))
if n >= 10:
    print('\nNão existe tabuada para números iguais ou superiores a 10.')
else:
    for c in range(1,10):
        print(f'{n} x {c} = {n * c}')

