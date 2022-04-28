from time import sleep


print('Número por Extenso')

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = 'S'
while resp in 'Ss':
    while True:
        num = int(input('\nDigite um número entre 0 e 20: '))
        if 0 <= num <= 20:
             break
        print('\nTente novamente.', end='')
    print(f'\nVocê digitou o número {cont[num]}')
    resp = input('\nQuer continuar? [S/N]\nR:').strip().lower()[0]
print('\nFinalizando...')
sleep(1)
print('Programa finalizado com êxito!')
