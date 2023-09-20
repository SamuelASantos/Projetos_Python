# Ex038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# Autor - Samuel Santos

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num1 < num2:
    print('O SEGUNDO número é o maior.')
else:
    print('Não existe um número maior. Os dois valores são iguais.')
