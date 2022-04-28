print('Vários números com flag\n')

c = s = 0
while True:
    n = int(input('Insira um valor [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} valores e a soma deles é {s}.')
