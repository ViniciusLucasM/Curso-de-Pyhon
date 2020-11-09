# nota1 = float(input('Digite a sua primeira nota: '))
# nota2 = float(input('Digite a sua segunda nota: '))
# media = (nota1 + nota2) / 2
# if media < 5.0:
#    print('\033[1;31mVOCÊ FOI REPROVADO!!\033[m')
#    print('SUA MÉDIA FOI DE \033[1;31m{:.1f}\033[m'.format(media))
# elif media >= 5.0 and media <= 6.9:
#    print('\033[1;34mVOCÊ ESTÁ DE RECUPERAÇÃO!!\033[m')
#    print('SUA MÉDIA FOI DE \033[1;34m{:.1f}\033[m'.format(media))
# elif media >= 7.0:
#    print('\033[1;32mPARABÉNS, VOCÊ ESTÁ APROVADO!!\033[m')
#    print('SUA MÉDIA FOI DE \033[1;32m{:.1f}\033[m'.format(media))


# CÓDIGO DO PROFESSOR
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(
    nota1, nota2, media))
if 7 > media >= 5:
    print('O Aluno está de RECUPERAÇÃO.')
elif media < 5:
    print('O Aluno está REPROVADO.')
elif media >= 7:
    print('O Aluno está APROVADO.')
