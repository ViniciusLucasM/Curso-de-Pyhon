num = int(input('Digite um numero para ver a tabuada: '))
resu = 0
for c in range(1, 11):
    for z in range(1, 11):
        if c == num:
            resu = c * z
            print('{} x {} = {}'.format(num, z, resu))
