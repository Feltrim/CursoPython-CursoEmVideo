print('Detector de Palíndromo\n')

frase = input('Digite uma frase:\nR: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')
