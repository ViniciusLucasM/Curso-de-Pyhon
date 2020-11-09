Vcasa = float(input('Digite o valor da casa desejada: R$ '))
Vsala = float(input('Digite a sua quantia salarial: R$ '))
Anos = int(input('Digite o tanto de anos que deseja parcelar: '))
presta = Vcasa / (Anos * 12)
exSal = (Vsala * 30) / 100
if presta > exSal:
    print('Infelizmente o seu crédito não foi aprovado.')
    print('O valor das parcelas ficaria em R${:.2f} ao Mês'.format(presta))
else:
    print('PARABÉNS, seu crédito foi aprovado.')
    print('O valor das parcelas será R${:.2f} ao Mês'.format(presta))
