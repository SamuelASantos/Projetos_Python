# Ex026 - Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
# Autor - Samuel Santos

frase = str(input('Digite uma frase: ')).strip()

print(f'A letra A aparece {frase.lower().count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.upper().find("A")}.')
print(f'A última letra A apareceu na posição {frase.lower().rfind("a")}')
