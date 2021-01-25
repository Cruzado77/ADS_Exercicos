###Raphael Rodrigues de Sena

print('Banco Ouro de Trouxa S.A.')
print('Para saber o valor de seu crédito especial disponível...')
saldo = int(input('Digite sua média de saldo anual : '))

if saldo <= 200:
    credito = 0
elif saldo <= 400:
    credito = saldo * 0.2
elif saldo <= 600:
    credito = saldo * 0.3
elif saldo > 600:
    credito = saldo * 0.4

print(f'Para um saldo médio de {saldo}% está disponível um crédito de {credito}%! ')