print('Super Progressão Aritmética v3.0\n')

n1 = int(input('Digite o primerio termo: '))
r = int(input('Digite a razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{n1} → ', end='')
        n1 += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?\nR: '))
print(f'Progressão finalizada com {total} termos mostrados.')
