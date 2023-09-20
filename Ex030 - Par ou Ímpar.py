# Ex030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
# Autor - Samuel Santos

num = int(input('Me diga um número qualquer: '))

print(f"O número {num} é PAR" if num % 2 == 0 else f"O número {num} é ÍMPAR")
