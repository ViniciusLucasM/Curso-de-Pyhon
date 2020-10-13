cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

lista = cidade.split()
print('A sua cidade começa com a palavra Santo? {}'.format(
    'SANTO' in lista[0]))


# CÓDIGO FEITO PELO PROFESSOR
# cid = str(input('Digite a cidade que você nasceu: ')).strip()
# print(cid:5.upper() == 'SANTO')
