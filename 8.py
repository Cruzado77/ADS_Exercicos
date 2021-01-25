###Montar uma aplicação que receba o nome de um aluno, suas quatro notas e calcule e exiba
###a sua média final. A aplicação deverá exibir também a situação final desse aluno
###(Aprovado/Recuperação/Reprovado).

###RAPHAELRODRIGUES DE SENA

class Aluno:
    nome = ""
    notas = []
    def __init__(self,nome,notas):
        super().__init__()
        self.nome = nome
        self.notas = notas

    def GetMedia(self):
        return sum(self.notas)/len(self.notas)

    def GetSituation(self):
        med = self.GetMedia()
        if(med > 7):
            return "Aprovado(Nas nuvens)"

        if(med > 3):
            return "em Recuperação(Nas mãos e Deus)"
        if(med < 3):
            return "Reprovado(Lascado)"

while(True):
    try:
        notas = []

        nome = input('Digite o nome do cabra :')

        for i in range(0,4):
            print(f'Digite a {i+1}ª nota: ')
            x = float(input())
            if(x<0) | (x>10):
                raise Exception("Notas >= 0 ou <= 10")
            else:
                notas.append(x)

        aluno = Aluno(nome,notas)

        print(f'Cidadão {aluno.nome} tem média {aluno.GetMedia():.2f} e está {aluno.GetSituation()}')
        break
    except:
        print('Digite errado não que eu não tenho o dia todo!!!')
        continue