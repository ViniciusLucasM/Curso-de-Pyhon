decimal = int(input('Digite um número decimal: '))

print('[ 1 ] Converter para Binário')
print('[ 2 ] Converter para Octal')
print('[ 3 ] Converter prar Hexadecimal')
op = int(input('Digite a opção desejada: '))
if op == 1:
    print('O número {} convertido para binário é {}'.format(
        decimal, bin(decimal)[2:]))
elif op == 2:
    print('O número {} convertido para Octal é {}'.format(
        decimal, oct(decimal)[2:]))
elif op == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(
        decimal, hex(decimal)[2:]))
else:
    print('DIGITE UMA OPÇÃO VALIDA')
