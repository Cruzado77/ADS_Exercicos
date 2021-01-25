###Raphael Rodrigues de Sena

x = int(input('Digite um valor : '))
y = int(input('Digite um valor : '))
z = int(input('Digite um valor : '))

if(x < (y + z)) & ((y < (x + z)) & (z < (x + y))):
    print('Os valores podem descrever os lados de um triângulo')
    if (x == y) & (x == z):
        triangulo = "equiátero"
    elif ((x == y) | ((x == z) | (y == z))):
        triangulo = "isósceles" 
    else:
        triangulo = "escaleno"
    print(f'Compõem lados de um triangulo {triangulo}!')
else:
    print('Os valores não compõem um triangulo!')