import os
import time

opcao = 0

while True:
    print('\n\nVamos utilizar um Temporizador (Decrementa o tempo definido) ou Contador (Incrementa até o limite definido)')
    print('\n\n Escolha qual deseja utiliza:')
    print('\n 1 - Temporizador')
    print('\n 2 - Contador')
    print('\n 3 - Sair')
    opcao = int(input('\nDigite a opção desejada: '))
    
    if opcao not in [1, 2, 3]:
        os.system('cls')
        print('\nOpção Inválida!')
    elif opcao == 1:
        os.system('cls')
        t = int(input('\n\nDeseja uma contagem regressiva a partir de: '))
        for i in range(t, -1, -1):
            print(f'\n{i}')
            time.sleep(1)
    elif opcao == 2:
        os.system('cls')
        t = int(input('\n\nDeseja contar até: '))
        for i in range(0, t+1, 1):
            print(f'\n{i}')
            time.sleep(1)
    elif opcao == 3:
        os.system('cls')
        print('\n\n\n\n\n\n\nFinalizando o tempo!\n\n\n\n\n')
        exit()
        
        