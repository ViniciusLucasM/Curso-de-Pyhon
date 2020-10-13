km = int(input('Digite a velocidade do carro: '))
vMulta = (km - 80) * 7
if km > 80:
    print('VOCÊ FOI PEGO EM ALTA VELOCIDADE!')
    print('VOCÊ ESTA TOMANDO UMA MULTA DE R${}'.format(vMulta))
else:
    print('VOCÊ ESTA NA VELOCIDADE QUE A PISTA PERMITE, PARABÉNS!')
