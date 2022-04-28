from datetime import datetime


print('Cadastro de Trabalhador em Python\n')

dados = {}
dados['Nome'] = input('Nome\n>>>>> ')
nasc = int(input('Ano de nascimento\n>>>>> '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho\n>>>>> '))
if dados ['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário\n>>>>> R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print()
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor de {v}')
