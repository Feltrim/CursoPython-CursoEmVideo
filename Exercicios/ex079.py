print('Valores únicos em uma Lista\n')

numeros = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = input('Quer continuar? [S/N]\nR: ')
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
