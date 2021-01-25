###Escrever um programa que leia o nome e a data de nascimento (dia, mês e ano) de uma
###pessoa e calcule a idade atual dele. Exibir o nome e a idade calculada.

###RAPHAEL RODRIGUES DE SENA

class Data:
    def __init__(self):
        super().__init__()
    def setData(self,dia,mes,ano):
        super().__init__()
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def InputData(self):
        self.dia = int(input('Dia :'))
        self.mes = int(input('Mês :'))
        self.ano = int(input('Ano :'))

class Pessoa:
    def __init__(self,nome,nascimento):
        super().__init__()
        self.nome = nome
        self.nascimento = nascimento

def CalcIdade(nascimento,atual):
    res = Data()
    
    if(nascimento.ano < atual.ano):
        res.ano = atual.ano - nascimento.ano
    else:
        print('Datas inválidas!')
        
    if(nascimento.mes < atual.mes):
        res.mes = atual.mes - nascimento.mes
    else:
        res.ano -=1
        res.mes = 12 + atual.mes - nascimento.mes
        
    if(nascimento.dia < atual.dia):
        res.dia = atual.dia - nascimento.dia
    else:
        res.mes -= 1
###Mês padrão de 30 dias para facilitar minha vida
        res.dia = 30 + atual.dia - nascimento.dia
    
    if res.mes == 0:
        res.mes = 12
        res.ano -= 1

    return res


def ViewIdade(pessoa,atual):
    idade = CalcIdade(pessoa.nascimento,atual)
    print(f'A idade de {pessoa.nome} são aproximadaos {idade.ano} anos, {idade.mes} meses e {idade.dia} dias!')

    
nome = input('Digite o nome do fulano: ')
print('Sete a data de nascimento:')
nascimento = Data()
nascimento.InputData()

print('Sete a data atual:')
atual = Data()
atual.InputData()

fulano = Pessoa(nome,nascimento)

ViewIdade(fulano,atual)