tabu = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for c in range(0, 9):
    num1 = tabu[c]
    print('=' * 13)
    for z in range(1, 10):
        resu = num1 * z
        print('{} x {} = {}'.format(num1, z, resu))