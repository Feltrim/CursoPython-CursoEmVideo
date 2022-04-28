from time import sleep


print('Cálculo do Fatorial\n')

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'\nCalculando...')
sleep(1)
print(f'\n{n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
