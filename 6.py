###Desenvolva um programa em python que leia o nome e a idade de 3 pessoas e mostre o nome
###da pessoa mais velha e o nome da pessoa mais nova.

###RAPHAEL RODRIGUES DE SENA


class Pessoa:
    nome = ""
    idade = 0
    def __init__(self,nome,idade):
        super().__init__()
        self.nome = nome
        self.idade = idade
    def GetObjIdade(self):
        return self.idade

def GetIdade(pessoa):
    return pessoa.idade

try:
    pessoas = []

    for i in range(0,3):
        print(f'Definindo o {i+1}º cidadão:')
        x = input('Nome : ')
        y = int(input('Idade : '))
        pessoas.append(Pessoa(x,y))



    print(f'A pessoa mais velha é {max(pessoas,key=GetIdade).nome}')
    print(f'A pessoa mais nova é {min(pessoas,key=GetIdade).nome}')

except:
    print('Valor Inválido!')