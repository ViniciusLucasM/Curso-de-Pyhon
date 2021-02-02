import random

capital_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = capital_case.lower()
numbers = '0123456789'
symbols = '!@#$%&*'
list_options = ['']
pswd = ''
size = 0
ammount = 0

op = str(input('PRESS ENTER TO ENTER THE PROGRAM...'))

if op == '':
    print('-=-'*10)
    print('WELCOME TO THE PASSWORD GENERATOR')
    print('-=-'*10)
    print()
    print('-=-'*13)
    print('CHOOSE THE CHARACTERS YOU WANT')
    print('-=-'*13)

    while op != '9':
        capital, lower, number, symbol = False, False, False, False
        pswd = ''
        if size <= 0 or ammount <= 0:
            size = int(
                input('TYPE HOW MANY CHARACTERS YOUR PASSWORD WILL HAVE:'))
            ammount = int(input('TYPE HOW MANY PASSWORDS YOU WISH:'))
            print()
        else:
            print()
            print('( 1 ) CAPITAL CASE')
            print('( 2 ) LOWER CASE')
            print('( 3 ) NUMBERS')
            print('( 4 ) SYMBOLS')
            print('( 9 ) CLOSE PROGRAM')
            op = input('SELECT THE OPTION YOU WISH: ')
            list_options = op.strip().replace(
                ',', ' ').replace('.', ' ').replace('', ' ').split()
            for a in range(len(list_options)):
                options = int(list_options[a])
                if options == 1:
                    capital = True
                    pswd += capital_case
                if options == 2:
                    lower = True
                    pswd += lower_case
                if options == 3:
                    if capital is False and lower is False:
                        print()
                        print('THE PASSWORD CANNOT BE GENERATED ONLY WITH '
                              'NUMBERS')
                    else:
                        number = True
                        pswd += numbers
                if options == 4:
                    if capital is False and lower is False:
                        print()
                        print('THE PASSWORD CANNOT BE GENERATED ONLY WITH '
                              'SYMBOLS')
                    else:
                        symbol = True
                        pswd += symbols
                if options == 9:
                    print('THANK YOU VERY MUCH FOR USING OUR PASSWORD '
                          'GENERATOR')
                    op = str('9')
                if options == 0:
                    print()
                    print('PLEASE SELECT ANY OPTION')
            print()
            for b in range(ammount):
                if pswd != '':
                    senha = ''.join(random.sample(pswd, size))
                    print(senha)
