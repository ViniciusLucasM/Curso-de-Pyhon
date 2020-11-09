dia = input('Qual é o seu dia de nascimento?  ')
mes = input('Qual é o seu mês de nascimento?  ')
ano = input('Qual é o seu ano de nascimento?  ')

print('Você nasceu no dia , \033[1;31m{}\033[m de \033[1;32m{}\033[m de \033[1;33m{}\033[m. Correto?'.format(
    dia, mes, ano))
