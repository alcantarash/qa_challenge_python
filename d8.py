import os
import time

tarefas = []
opcao = 0

while True:
    os.system('cls')
    print('\n\nGerenciando sua Lista de Tarefas')
    print('\n\n O que deseja fazer?')
    print('\n 1 - Listar Tarefas')
    print('\n 2 - Cadastrar Tarefa')
    print('\n 3 - Excluir Tarefa')
    print('\n 4 - Sair')
    opcao = int(input('\nDigite a opção desejada: '))
    
    if opcao not in [1, 2, 3, 4]:
        os.system('cls')
        print('\nOpção Inválida!')
    elif opcao == 1:
        os.system('cls')
        if len(tarefas) > 0:
            print('\n\n\n Lista de Tarefas \n')
            for i in tarefas:
                print(f'\n{int(tarefas.index(i)) + 1} -> {i}')
        else:
            print('Sem tarefas por enquanto!')
    elif opcao == 2:
        os.system('cls')
        t = input('Qual tarefa deseja gravar? ')
        tarefas.append(t)
    elif opcao == 3:
        os.system('cls')
        if len(tarefas) > 0:
            print('\n\n\n Lista de Tarefas \n')
            for i in tarefas:
                print(f'\n{int(tarefas.index(i)) + 1} -> {i}')
            t = int(input('\n\nDigite o numero da tarefa que deseja apagar: '))
            tarefa_deletada = tarefas[t - 1]
            decisao = input(f'Certeza que deseja apagar a tarefa \'{tarefa_deletada}\' ? S ou N ')
            if decisao == 'S':
                tarefas.pop(t - 1)
                print('Tarefa apagada!')
                
        else:
            print('Sem tarefas por enquanto!')
        
        
    elif opcao == 4:
        os.system('cls')
        print('\n\n\n\n\n\n\nFinalizando o tempo!\n\n\n\n\n')
        exit()
        
        