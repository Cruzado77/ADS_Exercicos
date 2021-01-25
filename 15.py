###Raphael Rodrigues de Sena
import math;

def Discriminante(a,b,c):
    return (b*b)-(4*a*c)


print('Descriminante da equação:')

a = float(input('Valor de a :'))
b = float(input('Valor de b :'))
c = float(input('Valor de c :'))

discriminante = Discriminante(a,b,c)

if discriminante == 0:
    print(f'Única raiz : {((-b)/(2*a)):.2f}!')
elif discriminante < 0:
    print('Raízes imaginárias!')
else:
    print(f'Primeira raiz : {((-b + (math.sqrt(discriminante)))/(2 * a)):.2f}')
    print(f'Segunda  raiz : {((-b - (math.sqrt(discriminante)))/(2 * a)):.2f}')