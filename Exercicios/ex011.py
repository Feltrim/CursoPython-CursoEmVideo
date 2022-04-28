print('Pintando Parede\n')

altura = float(input('Qual a altura da sua parede? R: '))
largura = float(input('Qual a largura da sua parede? R: '))
area = altura * largura
tinta = area / 2
print(f'A área da sua parede é igual a {area:.2f}m²')
print(f'Você precisará utilizar {tinta:.2f}L de tinta para cobrir essa área')
