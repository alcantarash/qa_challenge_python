print('Realizando Conversões')

opcao = 0

while opcao != 7:
    
    print('\nSelecione a opção para conversão:')
    print('\n1 - Quilômetros para Milhas')
    print('\n2 - Milhas para Quilômetros')
    print('\n3 - Metros para Pés')
    print('\n4 - Pés para Metros')
    print('\n5 - Graus Celsius para Fahrenheit')
    print('\n6 - Graus Fahrenheit para Celsius')
    print('\n7 - Sair')

    opcao = int(input('\n\nQual a opção desejada? '))
    
    if opcao not in range(1,7):
        print('Opção Incorreta!')
    else:
        valor = float(input('\nQual o valor a ser convertido? '))
    
        if opcao == 1:
            print(f"{valor} Quilômetro(s) é igual a {valor*0.621371} Milhas")
        elif opcao == 2:
            print(f"{valor} Milha(s) é igual a {valor*1.60934} Quilômetros")
        elif opcao == 3:
            print(f"{valor} Metro(s) é igual a {valor*3.28084} Pé(s)")
        elif opcao == 4:
            print(f"{valor} Pé(s) é igual a {valor/0.3048} Metro(s)")
        elif opcao == 5:
            print(f"{valor} Celsius é igual a {(valor- 32)* 5/9} Fahrenheit")
        elif opcao == 6:
            print(f"{valor} Fahrenheit  é igual a {valor/0.3048} Celsius")
            

