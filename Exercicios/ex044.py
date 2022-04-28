print('Gerenciador de Pagamentos\n')

preco = float(input('Qual o preço do produto?\nR$'))
print('''\nEscolha um método de pagamento:
[ 1 ] à vista no Dinheiro / Cheque
[ 2 ] à vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opcao = int(input('\nSua opção: '))
if opcao == 1:
    total = preco - preco / 10
    print(f'\nSua compra de R${preco:.2f} à vista no Dinheiro ou Cheque ficará no valor de R${total:.2f}.')
elif opcao == 2:
    total = preco - preco / 100 * 5
    print(f'\nSua compra de R${preco:.2f} à vista no Cartão ficará no valor de R${total:.2f}.')
elif opcao == 3:
    valorParc = preco / 2
    print(f'\nSua compra de R${preco:.2f} será parcelada em 2x de R${valorParc:.2f} no Cartão.')
    print(f'O valor continuará sendo de R${preco:.2f}.')
elif opcao == 4:
    total = preco + preco / 10 * 2
    qtdeParc = int(input('\nQuantas parcelas?\nR: '))
    if qtdeParc <= 2:
        print('\nSelecione uma quantidade de 3 ou mais parcelas.')
    else:
        valorParc = total / qtdeParc

        print(f'\nSua compra de R${preco:.2f} será parcelada em {qtdeParc}x parcelas de R${valorParc:.2f} no cartão.')
        print(f'Com o adicional de 20% de juros sua compra passará a valer R${total:.2f}')
else:
    print('\nArgumento inválido. Tente novamente.')
