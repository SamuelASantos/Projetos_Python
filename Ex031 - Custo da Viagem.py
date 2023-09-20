# Ex031 - Desenvolva um programa que pergunte a distância de uma veagem em Km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
# Autor - Samuel Santos

dist = float(input('Qual a distância da viagem? '))

print(f'Você está prestes a começar uma viagem de {dist} km.')
print(f'E o preço da sua passagem será de R$ {(dist * 0.50):.2f}' if dist <= 200 else f'E o preço da sua passagem será de R$ {(dist * 0.45):.2f}')
