print('Primeira e última ocorrência de uma string\n')

frase = input('Insira uma frase: ').strip().lower()
apareceu = frase.count('a')
posicao1 = frase.find('a') + 1
posicao2 = frase.rfind('a') + 1

if posicao1 >= 1:
    print(f'\nA letra "A" apareceu na frase {apareceu} vezes')
    print(f'A letra "A" apareceu na frase pela primeira vez na {posicao1}ª posição')
    print(f'A letra "A" apareceu na frase pela última vez na {posicao2}ª posição')

else:
    print('\nA letra "A" não apareceu nenhuma vez na frase.')
