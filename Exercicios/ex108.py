from modulos import ex108

print('Formatando Moedas em Python\n')

p = float(input('Digite o preço\nR$'))
print(f'A metade de {ex108.moeda(p)} é {ex108.moeda(ex108.metade(p))}')
print(f'O dobro de {ex108.moeda(p)} é {ex108.moeda(ex108.dobro(p))}')
print(f'Aumentando 10% temos {ex108.moeda(ex108.aumentar(p, 10))}')
