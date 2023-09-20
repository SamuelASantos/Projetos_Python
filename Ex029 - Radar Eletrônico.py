# Ex029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite
# Autor - Samuel Santos

vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print(
        f'Multado! Você excedeu o limite de velocidade que é de 80km/h\nVocê deve pagar uma multa de R$ {(vel - 80) * 7:.2f}!')

print('Tenha um bom dia! Dirija com segurança.')