from random import randint
from time import sleep


print('Palpites para a Mega Sena\n')

lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('\nQuantos jogos você quer que eu sorteie?\n>>>>> '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '=-' * 3)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
