print('Tabuada\n')

n = int(input('Insira um número: '))
if n <= 9:
    print('\n')
    print( '-' * 20)
    print('\n')

    print(f'A tabuada de {n} é:')
    print(f'{n} x 1 = {n * 1}')
    print(f'{n} x 2 = {n * 2}')
    print(f'{n} x 3 = {n * 3}')
    print(f'{n} x 4 = {n * 4}')
    print(f'{n} x 5 = {n * 5}')
    print(f'{n} x 6 = {n * 6}')
    print(f'{n} x 7 = {n * 7}')
    print(f'{n} x 8 = {n * 8}')
    print(f'{n} x 9 = {n * 9}')

    print('\n')
    print('-' * 20)

else:
    print(f'\nNão existe tabuada para números maiores que 9')
