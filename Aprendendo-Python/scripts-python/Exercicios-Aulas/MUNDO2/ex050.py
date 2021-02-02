soma = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        pares = num
        soma += pares
print('A soma dos números pares é {}'.format(soma))
