from random import randint
from time import sleep


print('GAME: Pedra Papel e Tesoura\n')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\nQual a sua jogada?\nR: '))

if jogador >= 3:
    print('\nJOGADA INVÁLIDA!')
else:
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    sleep(0.5)
    print('\n')
    print('-=' * 15)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 15)
    # Computador jogou PEDRA:
    if computador == 0:
        if jogador == 0:
            print('\nResultado: EMPATE')
        elif jogador == 1:
            print('\nResultado: JOGADOR VENCE')
        else:
            print('\nResultado: COMPUTADOR VENCE')
    # Computador jogou PAPEL
    elif computador == 1:
        if jogador == 0:
            print('\nResultado: COMPUTADOR VENCE')
        elif jogador == 1:
            print('\nResultado: EMPATE')
        else:
            print('\nResultado: JOGADOR VENCE')
    # Computador jogou TESOURA
    else:
        if jogador == 0:
            print('\nResultado: JOGADOR VENCE')
        elif jogador == 1:
            print('\nResultado: COMPUTADOR VENCE')
        else:
            print('\nResultado: EMPATE')
