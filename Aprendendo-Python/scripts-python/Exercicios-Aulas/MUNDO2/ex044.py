prePro = float(input('Digite o preço do produto desejado: R$'))
print('-=-' * 10)
print('SELECIONE A OPÇÃO DE PAGAMENTO')
print('-=-' * 10)
print('[ 1 ] PAGAMENTO NO DINHEIRO OU CHEQUE' '\n' '[ 2 ] PAGAMENTO NO CARTÃO' '\n' '[ 3 ] PRCELADO NO CARTÃO')
op = int(input('Digite a opção desejada: '))
if op == 1:
    descAvi = prePro - ((prePro * 10) / 100)
    print('Seu produto teve um desconto de 10% por pagamento avista, o valor final do produto é R${:.2f}'.format(
        descAvi))
elif op == 2:
    descAviC = prePro - ((prePro * 5) / 100)
    print('Seu produto teve um desconto de 5% por pagamento avista no cartão, o valor final do produto é R${:.2f}'.format(
        descAviC))
elif op == 3:
    par = int(input('Digite o tando de parcelas desejaveis: '))
    if par >= 1 and par <= 2:
        print(
            'O produto não sofreu alteração no seu valor, o preço final é de R${:.2f}'.format(prePro))
    elif par >= 3:
        juros = prePro + ((prePro * 20) / 100)
        print(
            'O preço do produto teve um juros de 20%, o preço final ficou em R${:.2f}'.format(juros))
else:
    print('POR FAVOR INSIRÁ UM OPÇÃO VALIDA. TENTE NOVAMENTE.')
# CÓDIGO DO PROFESSOR

# '{:=^40}' Esse formato serve para centralizar o texto informado no format, dessa forma o texto ficará centralizado dentro de quarenta espaços.
# print('{:=^40}'.format(' LOJAS GUANABARA '))
