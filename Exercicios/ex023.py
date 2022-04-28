print('Separando dígitos de um número\n')

numero = input('Digite um número entre 0 e 9999: ').strip()
tamanho = len(numero)
if tamanho > 4:
    print('\nO maior número permitido é 9999')

else:
    print(f'\nMilhar: {numero[0]}')
    print(f'Centena: {numero[1]}')
    print(f'Dezena: {numero[2]}')
    print(f'Unidade: {numero[3]}')
