from time import sleep
enter = str(input('Aperte ENTER para iniciar a contagem'))
print()
if enter == '':
    print('A contagem para o estouro dos fogos esta começando')
    print()
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('AEEE OS FOGOS ESTOURARAM')
