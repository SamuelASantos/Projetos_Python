# Ex036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
# Autor - Samuel Santos

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos_financiado = int(input('Quantos anos de financiamento? '))

mensal = (valor_casa / anos_financiado) / 12

print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiado} anos, a prestação será de R$ {(mensal):.2f}')
if mensal < (salario * 30 / 100):
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
