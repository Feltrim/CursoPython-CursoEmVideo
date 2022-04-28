from random import randint
from time import sleep

print('Jogo da Adivinhação v.1.0\n')

NumeroAleatorio = randint(0, 5)
NumeroEscolhido = int(input('Qual número entre 1 e 5 você acha que a máquina escolheu?\nR: '))

print('PROCESSANDO...')
sleep(3)
if NumeroEscolhido > 5:
    print('\nERRO!')
    print('\nEscolha apenas um número entre 1 e 5!')

elif NumeroEscolhido == NumeroAleatorio:
    print(f'\nParabéns, você acertou! O número escolhido pelo computador foi {NumeroAleatorio}.')

else:
    print(f'\nVocê errou! O número escolhido pelo computador foi {NumeroAleatorio}.')
    print('Mais sorte da próxima vez!')
