###Escrever um programa para calcular a temperatura em grau Celsius a partir da temperatura
###corrente medida em Farenheit. Utilizar a fórmula abaixo:
###C = (F-32) / 1,8

def GetCelsius(x):
    return (x - 32) / 18

try:
    x = float(input('Digite um valor em Farenheit : '))

    print(f'{x:.2f}ºF = {GetCelsius(x):.2f}ºC')

except:

    print('Valor Inválido!')