from datetime import date
anoParticipante = int(input('Digite o seu ano de nascimento: '))
genero = str(input('Digite o seu genêro: ')).upper().strip()
anoAtual = date.today().year
idade = anoAtual - anoParticipante
if genero == 'FEMININO':
    print('PARA MULHERES NÃO É NECESSÁRIO O ALISTAMENTO NO SERVIÇO MILITAR')
else:
    if idade == 18:
        print('Você tem {} anos, chegou a hora de se alistar no serviço militar.'.format(idade))
    elif idade > 18:
        prazo = idade - 18
        anoAlis = anoAtual - prazo
        print('Você tem {} anos, e perdeu seu ano de alistamento, compareça imediatamente a uma unidade pra se alistar'. format(idade))
        print('Você está a {} anos sem se alistar'.format(prazo))
        print('O seu ano de alistamento foi em {}'.format(anoAlis))
    elif idade < 18:
        prazo = 18 - idade
        anoAlis = anoAtual + prazo
        print('Você tem {} anos, então ainda não chegou a hora de se alistar no serviço militar.'.format(idade))
        print('Ainda falta {} anos para você se alistar.'.format(prazo))
        print('O seu ano de alistamento será em {}'.format(anoAlis))
