sal = float(input('Digite o valor do seu salário: '))
if sal > 1250.00:
    aum = (sal * 0.10) + sal
    print(
        'VOCÊ RECEBEU UM AUMENTO DE 10%, SEU SALÁRIO'
        'FOI REAJUSTADO PARA R${:.2f}'.format(aum))
else:
    aum = (sal * 0.15) + sal
    print(
        'VOCÊ RECEBEU UM AUMENTO DE 15%, SEU SALÁRIO'
        'FOI REAJUSTADO PARA R${:.2f}'.format(aum))
