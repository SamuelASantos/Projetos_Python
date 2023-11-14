"""
    Ex070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
    continuar. No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$ 1000,00.
    C) qual é o nome do produto mais barato.
    Autor - Samuel Santos
    Empresa - samsantos
"""

total = mais_mil = cont = menor_preco = 0
mais_barato = ''

print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        mais_mil += 1
    if cont == 0:
        mais_barato = produto
        menor_preco = preco
    else:
        if preco < menor_preco:
            mais_barato = produto
            menor_preco = preco
    cont += 1
    while True:
        escolha = input('Quer continuar? [S/N] ').strip().upper()
        if escolha[0] in 'SN':
            break
    if escolha[0] == 'N':
        break

print('-' * 10, end=' ')
print('FIM DO PROGRAMA', end=' ')
print('-' * 10)
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {mais_barato} que custa R$ {menor_preco:.2f}')
