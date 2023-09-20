# Ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Autor - Samuel Santos

m = float(input('Uma distância em metros: '))

print(f'A medida de {m}m corresponde a:')
print(f'{m / 1000} km')
print(f'{m / 100} hm')
print(f'{m / 10} dam')
print(f'{m * 10} dm')
print(f'{m * 100} cm')
print(f'{m * 1000} mm')
