'''
    Ex053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíngromo, desconsideando os espaços.
    Ex:
    - APOS A SOPA
    - A SACADA DA CASA
    - A TORRE DA DERROTA
    - O LOBO AMA O BOLO
    - ANOTARAM A DATA DA MARATONA
    Autor - Samuel Santos
    Empresa - samsantos
'''
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
frase_reversa = frase[::-1]

print(f'O inverso de {frase} é {frase_reversa}')
if frase == frase_reversa:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
