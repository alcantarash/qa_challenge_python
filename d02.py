print('Vamos realizar as operações!')

while True:
    
    print('\n1 - Soma')
    print('\n2 - Subtração')
    print('\n3 - Multiplicação')
    print('\n4 - Divisão')
    op = int(input('\nQual operação deseja? '))
    
    print('\nAgora digite os números: ')
    n1 = float(input('\nDigite o primeiro número: '))
    n2 = float(input('\nDigite o segundo número: '))
    
    if op == 1:
        resultado = n1+n2
        print(n1, ' + ', n2, ' = ', resultado)
    elif op == 2:
        resultado = n1-n2
        print(n1, ' - ', n2, ' = ', resultado)
    elif op == 3:
        resultado = n1*n2
        print(n1, ' * ', n2, ' = ', resultado)
    elif op == 4:
        if n2 == 0:
            print('Divisão por 0 não é possível!')
        else:
            resultado = n1-n2
            print(n1, ' / ', n2, ' = ', resultado)    
    