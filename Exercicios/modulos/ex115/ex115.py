from lib.interface import *
from lib.arquivo import *
from time import sleep

print('A) Criando um menu em Python')
print('B) Arquivos com Python')
print('C) Finalizando o projeto\n')

arq = 'pessoasCadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = input('Nome\n>>>>> ')
        idade = leiaInt('Idade\n>>>>> ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m\n')
    sleep(2)
