num = int(input('Digite o número que você queira saber a tabuada: '))
for c in range(1, 11):
    resu = num * c
    print('{} x {} = {}'.format(num, c, resu))
