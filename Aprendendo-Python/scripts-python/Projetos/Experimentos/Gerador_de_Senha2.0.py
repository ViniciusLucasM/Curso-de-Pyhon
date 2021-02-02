import random

letras_maiu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minu = letras_maiu.lower()
numeros = '0123456789'
simbolos = '!@#$%&*'
lista_opcoes = []
senha = ''

print('==== BEM VINDO AO GERADOR DE SENHA ====')
print('SELECIONE AS OPÇÕES QUE DESEJA UTILIZAR')

for a in range(0, 4):
    print('')
    print('[ 1 ] UTILIZAR LETRAS MAIUSCULAS')
    print('[ 2 ] UTILIZAR LETRAS MINUSCULAS')
    print('[ 3 ] UTILIZAR NÚMEROS')
    print('[ 4 ] UTILIZAR SÍMBOLOS')
    op = int(input('DIGITE AS OPÇÕES QUE DESEJA UTILIZAR: '))
    lista_opcoes.append(op)
print(lista_opcoes)

senha_tamanho = int(input('DIGITE O TAMANHO DA SUA SENHA: '))
tanto_senhas = int(input('DIGITE QUANTAS SENHAS DESEJA GERAR: '))

for b in range(0, 4):
    opcao = lista_opcoes[b]
    if opcao == 1:
        senha += letras_maiu
        print('OK, LETRAS MAIÚSCULAS ADICIONADAS')
    elif opcao == 2:
        senha += letras_minu
        print('OK, LETRAS MINÚSCULAS ADICIONADAS')
    elif opcao == 3:
        senha += numeros
        print('OK, NUMEROS ADICIONADOS')
    elif opcao == 4:
        senha += simbolos
        print('OK, SIMBOLOS ADICIONADOS')
    else:
        print('OK')

for c in range(tanto_senhas):
    senhas = ''.join(random.sample(senha, senha_tamanho))
    print(senhas)
