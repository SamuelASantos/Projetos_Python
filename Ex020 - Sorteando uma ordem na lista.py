# Ex020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quarto alunos e mostre a ordem sorteada.
# Autor - Samuel Santos

from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação do trabalho será {lista}')
