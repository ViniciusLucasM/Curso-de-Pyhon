dia = int(input('Insira a quantidade de dias que o carro ficou alugado: '))
km = float(input('Insira a quantida de KM rodados: '))
valorf = (dia * 60) + (km * 0.15)
print('O total a pagar pelo aluguél do carro é R${:.2f}'.format(valorf))
