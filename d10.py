import os
import time
import random


tentativas = 7
randNum = random.randint(1, 100)

while True:

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