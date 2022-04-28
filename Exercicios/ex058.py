from random import randint

print('Jogo da Advinhação v2.0\n')

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\nQual é o seu palpite?\nR: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\nMais... Tente mais uma vez.')
        elif jogador > computador:
            print('\nMenos... Tente mais uma vez.')
print(f'\nAcertou com {palpites} tentativas. Parabéns!')
