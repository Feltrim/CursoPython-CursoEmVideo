from modulos import ex107

print('Exercitando módulos em Python\n')

p = float(input('Digite o preço\nR$'))
print(f'A metade de R${p} é R${ex107.metade(p)}')
print(f'O dobro de R${p} é R${ex107.dobro(p)}')
print(f'Aumentando 10% temos R${ex107.aumentar(p, 10)}')
