from datetime import date

print('Alistamento Militar\n')

nascimento = int(input('Em que ano você nasceu?\n'))

ano = date.today().year
idade = ano - nascimento

if idade == 17:
    print(f'\nAinda falta 1 ano para você se alistar')
elif idade < 18:
    print(f'\nAinda faltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print('\nJá está na hora de se alistar!')
elif idade == 19:
    print('\nEssa não! Você está atrasado 1 ano para o alistamento!')
else:
    print(f'\nEssa não! Você está atrasado {idade - 18} anos para o alistamento!')
