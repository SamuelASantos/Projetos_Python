'''
    Ex043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
    acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade mórbida
    Autor - Samuel Santos
'''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

print(f'Com o peso de {peso}kg e a altura de {altura}m, seu IMC é de {imc:.2f}')
if imc <= 18.5:
    print('Sua classificação é de ABAIXO DO PESO.')
elif imc <= 25:
    print('Sua classificação é de PESO IDEAL.')
elif imc <= 30:
    print('Sua classificação é de SOBREPESO.')
elif imc <= 40:
    print('Sua classificação é de OBESIDADE.')
else:
    print('Sua classificação é de OBESIDADE MÓRBIDA.')