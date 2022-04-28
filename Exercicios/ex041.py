from datetime import date

print('Classificando Atletas\n')

nascimento = int(input('Em que ano você nasceu?\nR:'))

ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('\nVocê é um atleta MIRIM')

elif 9 < idade <= 14:
    print('\nVocê é um atleta INFANTIL')

elif 14 < idade <= 19:
    print('\nVocê é um atleta JUNIOR')

elif 19 < idade <= 20:
    print('\nVocê é um atleta SÊNIOR')

else:
    print('\nVocê é um atleta MASTER')
