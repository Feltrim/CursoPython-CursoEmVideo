print('Primeiro e último nome de uma pessoa\n')

nome = input('Insira seu nome completo: ').strip()
ns = nome.split()

print(f'\nMuito prazer em te conhecer, {nome}!')
print(f'\nSeu primeiro nome é {ns[0]}?')
print(f'Seu último nome é {ns[-1]}?')
