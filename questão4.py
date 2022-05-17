print('Bem vindo ao controle de Estoque da Bicicletaria do Gustavo Soares Sousa')
pecas = []
peca = {}

def opção():
    print('Escolha a opção desejada:')
    print('1 - Cadastar peças')
    print('2 - Consultar peças')
    print('3 - Remover Peças')
    print('4 - Sair')
    opcao = int(input('>>'))

    if opcao == 1:
        cadastrarPeca()
    if opcao == 2:
        consultaPeca()
    if opcao == 3:
        removerPeca()
    return opcao


def cadastrarPeca():
    try:
        peca['codigo'] = int(input('Código da peça: '))
        peca['nome'] = input('Por favor entre com o NOME da peça: ')
        peca['fabricante'] = input('Por Favor entre com o FABRICANTE da peça: ')
        peca['valor'] = int(input('Por Favor entre com o valor(R$) da peça'))
        pecas.append(peca.copy())
        print(pecas)
    except ValueError as error:
        print(error)

def consultaPeca():
    print('Você selecionou a opção de consultar Peças')
    print('Escolha a opção desejada: ')
    print('1 - Consultar Todas as Peças')
    print('2 - Consultar Peças por Código')
    print('3 - Consultar Peças por Fabricante')
    print('4 - retornar')
    try:
        opcao = int(input('>>'))
        if opcao == 1:
            print(pecas)
        if opcao == 2:
            codigo = int(input('Digite o CÓDIGO da peça: '))
            for i in pecas:
                if i['codigo'] == codigo:
                    print(i)
                else:
                    print('Nenhum peça foi encontrada por esse código')
        if opcao == 3:
            fabricante = input('Digite o fabricante da peça')
            for i in pecas:
                if i['fabricante'] == fabricante:
                    print(i)
                else:
                    print('Nenhum fabricante encontrado')


    except ValueError as erro:
        print('Erro')


def removerPeca():
    print('Você Selecionou a Opção de Remover Peça')
    try:
        codigo = int(input('Digite o código da peca a ser removida'))
        for i in pecas:
            if i['codigo'] == codigo:
                pecas.remove(i)
            else:
                'Nenhum peça encontrada por esse código'
    except ValueError as error:
        print(error)


while True:
    opcao = opção()
    if(opcao == 4):
        break
    else:
        continue