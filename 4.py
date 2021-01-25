###Escrever um programa que leia dois valores quaisquer, calcule a diferença entre o maior e o
###menor, e em seguida exiba os três valores.

def Modulo(x):
    if(x<0):
        return x*(-1)
    else:
        return x;

def Diferenca(x,y):
    return Modulo(x-y)


try:

    x = float(input('Digite um valor : '))
    y = float(input('Digite um valor : '))

    print(f'|{x:.2f} - {y:.2f}| = {Diferenca(x,y):.2f}')

except:
    print('Valor inválido!')