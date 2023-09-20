'''
    Ex056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A média de idade do grupo
    - Qual é o nome do homem mais velho
    - Quantas mulheres têm menos de 20 anos
    Autor - Samuel Santos
    Empresa - samsantos
'''
media = 0
nome_h = ''
idade_h = 0
mulheres_menos20 = 0

for c in range(1, 5):
    print('=' * 25)
    print(f'\t\t{c}ª PESSOA')
    print('=' * 25)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M' and idade > idade_h:
        nome_h = nome
        idade_h = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1

print('=' * 25)
print(f'A média de idade do grupo é de {media/4:.1f} anos.')
print(f'O homem mais velho tem {idade_h} anos e se chama {nome_h}')
print(f'Ao todo são {mulheres_menos20} mulheres com menos de 20 anos.')
