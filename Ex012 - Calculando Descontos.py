# Ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
# Autor - Samuel Santos

preco = float(input('Qual é o preço do produto? R$ '))

print(f'O produto que custava R$ {preco:.2f}, na promoção com desconto de 5% vai custar R$ {(preco - (preco * 5 / 100)):.2f}')
