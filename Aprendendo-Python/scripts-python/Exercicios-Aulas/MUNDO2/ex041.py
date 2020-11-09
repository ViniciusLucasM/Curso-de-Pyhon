from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade >= 1 and idade <= 9:
    print('ELE(A) POSSUI {} ANO(S) E ESTÁ NA CATEGORIA DOS ATLETAS MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('ELE(A) TEM {} ANOS E ESTÁ NA CATEGORIA DOS ATLETAS INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('ELE(A) TEM {} ANOS E ESTÁ NA CATEGORIA DOS ATLETAS JUNIOR'.format(idade))
elif idade == 20:
    print('ELE(A) TEM {} ANOS E ESTÁ NA CATEGORIA DOS ATLETAS SÊNIOR'.format(idade))
elif idade > 20:
    print('ELE(A) TEM {} ANOS E ESTÁ NA CATEGORIA DOS ATLETAS MASTER'.format(idade))
