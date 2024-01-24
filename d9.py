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

pontos = 0
opcao = 0
randNum = 0

while True:

    randNum = random.randint(0, 100)
    primo = ehPrimo(randNum)

    print(f'\n\nAdvinhe se é um número primo \t\t\t\t Pontuação: {pontos}')
    print('\n\n Foi gerado um número entre 0 e 100, ele é:')
    print('\n 1 - Primo?')
    print('\n 2 - Não Primo?')
    print('\n\n\n \t\t\t\t\t\t\t\t\t\t3 - Regras')
    print('\t\t\t\t\t\t\t\t\t\t4 - Sair')
    opcao = int(input('\nQual a sua resposta? '))
    
    if opcao not in [1, 2, 3, 4]:
        print('\n\nOpção Inválida!')
        time.sleep(1)
        os.system('cls')
    elif opcao in [1, 2]:
        os.system('cls')
        if (primo == True and opcao == 1) or (primo == False and opcao == 2):
            print('\n\nAcertou! Parabéns!')
            pontos = pontos + 1
            time.sleep(1)
            os.system('cls')
        else:
            print('Não foi dessa vez! rs')
            pontos = pontos - 1
            time.sleep(1)
            os.system('cls')
    elif opcao == 3:
        os.system('cls')
        print('\t\t\t\t Regras')
        print('\n1 - Para cada acerto, o jogador ganha 1 ponto.')
        print('\n2 - Para cada erro, o jogador perde 1 ponto.')
        
    elif opcao == 4:
        os.system('cls')
        print('\n\n\n\n\n\n\nFinalizando o jogo!\n\n\n\n\n')
        exit()
        
