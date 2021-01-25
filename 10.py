###O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem
###do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
###distribuidor seja de 28% e os impostos de 45%, escreva um programa que leia o custo de
###fábrica de um carro e escreva o custo ao consumidor.

###Raphael Rodrigues de Sena

print('Simular Custos ao consumidor:')

fabrica = float(input('Qual o custo de fabricação? '))

total = fabrica + (fabrica * 0.28) + (fabrica * 0.45)
### ou
### total = fabrica + fabrica * (0.28 + 0.45)

print(f'Do custo de fabricação de R${fabrica:.2f} é esperado um valor final de R${total:.2f}!')