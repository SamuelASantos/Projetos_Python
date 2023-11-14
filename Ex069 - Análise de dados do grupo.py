"""
    Ex069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
    perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.
    Autor - Samuel Santos
    Empresa - samsantos
"""

mais_dezoito = total_homens = mulheres_novas = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo[0] in 'MF':
            break
    if idade > 18:
        mais_dezoito += 1
    if sexo[0] == 'M':
        total_homens += 1
    if sexo[0] == 'F' and idade < 20:
        mulheres_novas += 1
    while True:
        escolha = input('Quer continuar? [S/N] ').strip().upper()
        if escolha[0] in 'SN':
            break
    if escolha[0] == 'N':
        break

print('=' * 6, end=' ')
print('FIM DO PROGRAMA', end=' ')
print('=' * 6)
print(f'Total de pessoas com mais de 18 anos: {mais_dezoito}')
print(f'Ao todo temos {total_homens} homens cadastrados.')
print(f'E temos {mulheres_novas} mulheres com menos de 20 anos.')
