print('Estatísticas em produtos\n')

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do Produto\nR:')
    preco = float(input('Preço:\nR$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]\nR: ').strip().upper()[0]
    if resp == 'N':
        break
print('\n{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
