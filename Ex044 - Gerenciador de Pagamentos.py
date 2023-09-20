'''
    Ex044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
    condições de pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
    Autor - Samuel Santos
'''

compras = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print(f'Sua compra de R$ {compras:.2f} terá um desconto de 10% e no final, custará R$ {(compras - (compras * 10 / 100)):.2f}')
elif opcao == 2:
    print(f'Sua compra de R$ {compras:.2f} terá um desconto de 5% e no final, custará R$ {(compras - (compras * 5 / 100)):.2f}')
elif opcao == 3:
    print(f'Sua compra totalizou R$ {compras:.2f}')
else:
    print(f'Sua compra de R$ {compras:.2f} terá um acréscimo de 20% e no final, custará R$ {(compras + (compras * 20 / 100)):.2f}')
