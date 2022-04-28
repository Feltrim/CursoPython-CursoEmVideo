print('Procurando uma string dentro de outra\n')

nome = input('Qual o seu nome completo? ').strip()
silva = nome.lower().find('silva')

if silva == -1:
    print('\nSeu nome não possui "Silva"')

else:
    print('\nSeu nome possui "Silva"')