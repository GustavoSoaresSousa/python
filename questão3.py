print('Bem Vindo a Companhia de Logística Gustavo Soares Sousa')

def dimensoesObjeto():
    try:
        comprimentoEmCm = int(input('Digite o comprimento do objeto (em cm)'))
        larguraEmCm = int(input('Digite a largura do objeto (em cm)'))
        alturaEmCm = int(input('Digite a altura do objeto (em cm)'))
        volumeDoObjeto = float(comprimentoEmCm * larguraEmCm * alturaEmCm)
        print('O volume do objeto é (em cm): {}'.format(volumeDoObjeto))
        valor = 0
        if volumeDoObjeto >= 1000000:
            print('Não aceitamos volume do objeto com dimensões tão grandes')
            print('Entre com as dimensões desejadas')
            dimensoesObjeto()
        elif volumeDoObjeto >= 30000:
            valor = 50
        elif volumeDoObjeto >= 10000:
            valor = 30
        elif volumeDoObjeto >= 1000:
            valor = 20
        elif volumeDoObjeto < 1000:
            valor = 10
        return valor
    except ValueError as erro:
        pass


def pesoObjeto():

    multiplicadorDoPeso = 0
    try:
        peso = float(input('Digite o peso do objeto (em kg)'))
        if peso >= 30:
            print('Não aceitamos objetos tão pesados')
        elif peso >= 10:
            multiplicadorDoPeso = 3
        elif peso >= 1:
            multiplicadorDoPeso = 2
        elif peso >= 0.1:
            multiplicadorDoPeso = 1.5
        elif peso <= 0.1:
            multiplicadorDoPeso = 1
        return multiplicadorDoPeso
    except ValueError as erro:
        pass

def rotaObjeto(valueDasDimensoes, valueDosPesos):
    print('Selecione a rota do objeto:')
    print('BR - De Brasília para Rio de Janeiro')
    print('BS - De Brasília para São Paulo')
    print('RB - De Rio de Janeiro para Brasília')
    print('RS - De Rio de Janeiro para São Paulo')
    print('SR - De São Paulo para Rio de Janeiro')
    print('SB - De São Paulo para Brasília')
    rota = input('>>')
    if rota == 'BR':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1.5, valueDasDimensoes, valueDosPesos, 1.5))
    elif rota == 'BS':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1.2, valueDasDimensoes, valueDosPesos, 1.2))
    elif rota == 'RB':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1.5, valueDasDimensoes, valueDosPesos, 1.5))
    elif rota == 'RS':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1, valueDasDimensoes, valueDosPesos, 1))
    elif rota == 'SR':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1, valueDasDimensoes, valueDosPesos, 1))
    elif rota == 'SB':
        print('Total a pagar(R$): {} (dimensões: {} * peso: {}  * rota: {} )' .format(valueDasDimensoes * valueDosPesos * 1.2, valueDasDimensoes, valueDosPesos, 1.2))
    else:
        print('Você digitou uma Rota que não existe')
        print('Por favor entre com a rota desejada')


while True:
    valueDasDimensoes = dimensoesObjeto()
    if valueDasDimensoes is not None:
        while True:
            valueDoPeso = pesoObjeto()
            if valueDoPeso is not None:
                rotaObjeto(valueDasDimensoes, valueDoPeso)
                break
            else:
                print('Você digitou peso do objeto com valor não númerico')
        break
    else:
        print('Você digitou alguma dimensão do objeto com valor não numérico')
