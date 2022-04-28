from random import randint


print('Jogo do Par ou Ímpar\n')

v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P / I]\nR:').strip().upper()[0]
    print(f'\nVocê jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('\nVOCÊ VENCEU!')
            v += 1
        else:
            print('\nVOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\nVOCÊ VENCEU!')
            v += 1
        else:
            print('\nVOCê PERDEU')
            break
    print('\nVamos jogar novamente...\n')
print(f'\nGAME OVER! Você venceu {v} vezes.')
