import os
import time
import random

def validaNumero(digitado):
    try:
        float(digitado)
        return True
    except ValueError:
        print('Entrada Incorreta! Tente Novamente!')

listNum = []
decisao = ''

print('\t\t\t\tOrdenando uma lista')
while True:

    print('\t (F)inalizei minha lista.')
    print('\t\t\t\t\t\t\t\t\t\t\t(S)air')
    decisao = input('\nDigite uma das opções ou seu numero: ')
        
    if (decisao.upper() != 'S') and (decisao.upper() != 'F'):
        if(validaNumero(decisao)):
            listNum.append(int(decisao))
            print(f'{listNum} \n\n\n')

    elif decisao.upper() == 'F':
        os.system('cls')
        print(f'Sua lista ordenada é -> {sorted(listNum)}\n\n\n')
        time.sleep(1)
    elif decisao.upper() == 'S':
        os.system('cls')
        print('\n\nAté uma próxima camarada!')
        time.sleep(1)
        exit()