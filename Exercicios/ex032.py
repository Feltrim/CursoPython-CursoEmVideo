from datetime import date

print('Ano Bissexto\n')

Ano = int(input('Que ano você quer analisar?\n'))

if Ano == 0:
    Ano = date.today().year

if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print(f'O ano {Ano} é bissexto')

else:
    print(f'O ano {Ano} não é bissexto')
