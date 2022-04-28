from time import sleep

print('Um print especial\n')


def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


# Programa Principal
while True:
    texto = input('Escreva um texto\n>>>>> ')
    print()
    escreva(texto)
    print()
    resp = input('Quer continuar? [Sim / Não]\n>>>>> ').strip().upper()[0]
    print()
    if resp in 'N':
        print('Finalizando...')
        sleep(1)
        break
print('Programa finalizdo com sucesso! Volte sempre.')
