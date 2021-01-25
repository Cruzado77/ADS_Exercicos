###Escrever um programa que leia três valores, e identifique o maior valor dentre eles.
### RAPHAEL RODRIGUES DE SENA

try:
    array = []
    array.append(int(input('Digite um valor: ')))
    array.append(int(input('Digite um valor: ')))
    array.append(int(input('Digite um valor: ')))
    
    print(f'Maior em ({array[0]},{array[1]},{array[2]}) é {max(array)}')

except:

    print('Digite um número!!!')