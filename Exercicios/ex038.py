print('Comparando números\n')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2:
    print('\nO\033[1;34m PRIMEIRO VALOR\033[0;;m é maior')

elif n1 < n2:
    print('\nO\033[1;34m SEGUNDO VALOR\033[0;;m é maior')

else:
    print('\nNão existe valor maior, os dois são\033[1;32m IGUAIS')
