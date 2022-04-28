print('Progressão Aritmética v2.0\n')

n1 = int(input('Digite o primerio termo: '))
r = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print(f'{n1} → ', end='')
    n1 += r
    cont += 1
print('FIM')
