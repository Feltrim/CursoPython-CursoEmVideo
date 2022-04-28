print('Função que calcula área\n')


def area(a, b):
    m = a * b
    print(f'A de área de um terreno de {a}m por {b}m é de {m}m²')


# Programa Principal
n1 = int(input('Digite a\033[1;34m largura\033[m do terreno\n>>>>> '))
n2 = int(input('Digite o\033[1;34m comprimento\033[m do terreno\n>>>>> '))

area(n1, n2)
