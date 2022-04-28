print('Soma ímpares múltiplos de três\n')

s = 0
o = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        o += 1
print(f'A soma dos {o} valores solicitados é de {s}.')
