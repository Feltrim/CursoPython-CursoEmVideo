print('Maior e menor da sequência\n')

maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input(f'Qual o peso da {pess}ª pessoa?\nR: '))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior:.2f}Kg')
print(f'O menor peso foi de {menor:.2f}Kg')
