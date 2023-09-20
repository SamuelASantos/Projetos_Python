'''
    Ex055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
    Autor - Samuel Santos
    Empresa - samsantos
'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O peso maior lido foi de {maior:.1f} kg.')
print(f'O peso menor lido foi de {menor:.1f} kg.')
