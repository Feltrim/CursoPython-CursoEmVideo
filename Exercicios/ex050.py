print('Soma dos pares\n')

s = 0
o = 0
for c in range(1, 7):
    n = int(input('Insira um valor: '))
    if n % 2 == 0:
        s += c
        o += 1
print(f'A soma dos {o} valores pares indicados é {s}')
