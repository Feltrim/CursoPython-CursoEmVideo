def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\n\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m\n')
        else:
            valido = True
            return float(entrada)
