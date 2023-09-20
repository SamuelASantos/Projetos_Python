# Ex011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
# Autor - Samuel Santos

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = lar * alt
print(f'Sua parede tem a dimensão de {lar} x {alt} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {(area / 2):.1f} litros de tinta.')
