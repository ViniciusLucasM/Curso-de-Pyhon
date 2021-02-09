def anobissexto(ano):
    if ano >= 1900 and ano <= 10 * 5:
        div4 = ano % 4
        div100 = ano % 100
        div400 = ano % 400
        if div4 == 0 and div100 != 0 or div400 == 0:
            print(True)
        elif div4 != 0 and div100 == 0 or div400 != 0:
            print(False)


ano = int(input('Digite um ano: '))
anobissexto(ano)
