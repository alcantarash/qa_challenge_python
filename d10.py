import os
import time
import random

def ehPrimo(numero):
    divisivel = 0
    
    for i in range(1, numero + 1):
        if divisivel <= 2:
            if numero % i == 0:
                divisivel = divisivel + 1
    if divisivel == 2:
        return True
    else:
        return False

tentativas = 7
opcao = 0
randNum = random.randint(1, 100)

while True:

    print(f'{randNum}')
    if tentativas > 0:
    
        print(f'\n\nFoi gerado um número entre 1 e 100 \t\t\t\t Tentativas: {tentativas}')
        chute = int(input('\nQual seu chute? '))
        
        
        if chute == randNum:
            print('\n\nParabéns! Você acertou!')
            time.sleep(1)
            tentativas = 0
            exit()
        elif chute > randNum:
            os.system('cls')
            print('Chute acima do número rs')
            tentativas = tentativas - 1
            time.sleep(1)
        elif chute < randNum:
            os.system('cls')
            print('Chute abaixo do número rs')
            tentativas = tentativas - 1
            time.sleep(1)
    else:
        os.system('cls')
        print('\n\n\n\n\n\n\nInfelizmente acabatam as tentativas. Até a próxima!\n\n\n\n\n')
        exit()