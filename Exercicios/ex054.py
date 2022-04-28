from datetime import date


print('Grupo da Maioridade\n')

atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu?\nR: '))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'\nAo todo tivemos {totalmaior} pessoas maiores de idade.')
print(f'E também tivemos {totalmenor} pessoas menores de idade.')
