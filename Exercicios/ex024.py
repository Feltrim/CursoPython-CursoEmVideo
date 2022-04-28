print('Verificando as primeiras letras de um texto\n')

cidade = input('Em que cidade você nasceu? ').strip()
santo = cidade[:5].lower() == 'santo'

if santo is True:
    print('\nO nome da sua cidade começa com "Santo"')

else:
    print('\nO nome da sua cidade não começa com "Santo"')
