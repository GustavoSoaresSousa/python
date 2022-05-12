print('Bem Vindo a Loja do Gustavo Soares Sousa')
valorDoProduto = float(input('Entre com valor do produto: '))
valorDaQuantidade = int(input('Entre com valor da quantidade: '))

if valorDaQuantidade <= 9 :
    valorTotal = float(valorDoProduto * valorDaQuantidade)
    print('Valor sem desconto foi: {:.2f}' .format(valorTotal))
    print('Valor com desconto foi: {:.2f} (desconto 0%)' .format(valorTotal))
elif valorDaQuantidade <= 99:
    valorTotal = float(valorDoProduto * valorDaQuantidade)
    valorComDesconto = float(valorTotal * 5/100)
    print('Valor sem desconto foi: {:.2f}' .format(valorTotal))
    print('Valor com desconto foi: {:.2f} (desconto 5%)' .format(valorTotal - valorComDesconto))
elif valorDaQuantidade <= 999:
    valorTotal = float(valorDoProduto * valorDaQuantidade)
    valorComDesconto = float(valorTotal * 10/100)
    print('Valor sem desconto foi: {:.2f}' .format(valorTotal))
    print('Valor com desconto foi: {:.2f} (desconto 10%)' .format(valorTotal - valorComDesconto))
elif valorDaQuantidade > 1000:
    valorTotal = float(valorDoProduto * valorDaQuantidade)
    valorComDesconto = float(valorTotal * 15/100)
    print('Valor sem desconto foi: {:.2f}' .format(valorTotal))
    print('Valor com desconto foi: {:.2f} (desconto 15%)' .format(valorTotal - valorComDesconto))