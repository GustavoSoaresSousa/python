print('Bem vindo a Lanchonete do Gustavo Soares Sousa')
print('*****************Cardápio*****************')
print('| Codigo |       Descrição       | Valor  |')
print('|  100   |   Cachorro Quente     |  9,00  |')
print('|  101   | Cachorro Quente Duplo |  11,00 |')
print('|  102   |       X-Egg           |  12,00 |')
print('|  103   |       X-Salada        |  12,00 |')
print('|  104   |       X-Bacon         |  14,00 |')
print('|  105   |       X-Tudo          |  17,00 |')
print('|  200   |   Refrigerante lata   |  5,00  |')
print('|  201   |   Chá Gelado          |  4,00  |')

codigoDoPedido = int(input('Entre com um códido desejado: '))


def verifica():
    print('Desaja mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    simOuNao = int(input(''))
    if simOuNao == 1:
        return True
    else:
        return False


valorTotal = 0

while codigoDoPedido:
    if codigoDoPedido == 100:
        print('Você pediu um Cachorro quente no valor de 9,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 9.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 101:
        print('Você pediu um cachorro quente duplo no valor de 11,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 11.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 12.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 12.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 14.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 17.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 5.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido == 201:
        print('Você pediu um Chá gelado no valor de 4,00')
        simOuNão = verifica()
        valorTotal = valorTotal + 4.00
        if simOuNão == False:
            print('Valor Total: {}'.format(valorTotal))
            break
        else:
            codigoDoPedido = int(input('Entre com um códido desejado: '))
            continue
    if codigoDoPedido >= 100 or codigoDoPedido <= 105:
        print('Opção Inválida')
        codigoDoPedido = int(input('Entre com um códido desejado: '))
        continue
    else:
        break
