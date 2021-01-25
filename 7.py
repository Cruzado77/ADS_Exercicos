###Montar uma aplicação na qual o usuário informe dois números, a operação que deseja
###realizar (+, -, x, /), calcule e exiba o resultado da operação matemática.

###RAPHAEL RODRIGUES DE SENA

def Soma(x,y):
    return x+y

def Subtracao(x,y):
    return x-y

def Multiplicacao(x,y):
    return x*y

def Divisao(x,y):
    return x / y;

while(True):
    print('Escolha uma opção:\n1)Soma\n2)Subtração\n3)Multiplicação\n4)Divisão\n5)Sair\n')

    try:
        op = int(input())
    except:
        op = -1
    if(op>5) | (op<1):
        print('Opção inválida!')
        continue
    elif (op == 5):
        break;

    x = float(input('x = '))
    y = float(input('y = '))

    if(op == 1):
        operador = '+'
        res = Soma(x,y)
    elif(op == 2):
        operador = '-'
        res = Subtracao(x,y)
    elif(op == 3):
        operador = '*'
        res = Multiplicacao(x,y)
    elif(op == 4):
        try:
            operador = '/'
            res = Divisao(x,y)
        except:
            print('Divisão por zero não é permitida!')
            continue
    print(f'{x:.2f}{operador}{y:.2f} = {res:.2f}')
