peso1 = 2.5
peso2 = 3.5
peso3 = 4

nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))
nota3 = float(input('Digite a terceira nota : '))

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f'Média = {media:.2f}')