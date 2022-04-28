from time import sleep


print('Tabuada v3.0\n')

while True:
    n = int(input('\nQuer ver a tabuada de qual valor? [Digite um número negativo para finalizar]\nR: '))
    if n >= 10:
        print('\nNão existe tabuada para números iguais ou superiores a 10.')
    elif n < 0:
        print('Finalizando...')
        sleep(1)
        print('Programa finalizado com sucesso!')
        break
    else:
        print('')
        for c in range(1, 10):
            print(f'{n} x {c} = {n * c}')
