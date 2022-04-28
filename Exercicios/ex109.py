from modulos import ex109

print('Formatando Moedas em Python\n')

p = float(input('Digite o preço\nR$'))
print(f'A metade de {ex109.moeda(p)} é {ex109.metade(p, True)}')
print(f'O dobro de {ex109.moeda(p)} é {ex109.dobro(p, True)}')
print(f'Aumentando 10% temos {ex109.aumentar(p, 10, True)}')
print(f'Reduzindo 10% temos {ex109.diminuir(p, 10, True)}')
