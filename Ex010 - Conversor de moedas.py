# Ex010 - Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerar US$ 1,00 = R$ 3,27
# Autor - Samuel Santos

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))

print(f'Com R$ {dinheiro:.2f} você pode comprar U$ {(dinheiro / 3.27):.2f}')
