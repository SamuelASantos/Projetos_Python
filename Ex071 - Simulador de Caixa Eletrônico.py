"""
    Ex071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
    será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
    Autor - Samuel Santos
    Empresa - samsantos
"""
print('=' * 30)
print(f'{"BANCO SAMSANTOS":^30}')
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))

while True:
    if valor == 0:
        break
    quant = int(valor / 50)
    print(f'Total de {quant} cédulas de R$ 50,00')
    valor -= 50 * quant
    if valor == 0:
        break
    quant = int(valor / 20)
    print(f'Total de {quant} cédulas de R$ 20,00')
    valor -= 20 * quant
    if valor == 0:
        break
    quant = int(valor / 10)
    print(f'Total de {quant} cédulas de R$ 10,00')
    valor -= 10 * quant
    if valor == 0:
        break
    quant = int(valor / 1)
    print(f'Total de {quant} cédulas de R$ 1,00')
    valor -= 1 * quant

print('=' * 30)
print('Volte sempre ao BANCO SAMSANTOS! Tenha um bom dia!')
