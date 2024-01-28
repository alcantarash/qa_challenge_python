import string

print('Identificando um Palíndrimo!')


word = input('\nDigite sua palavra ou expressão: ')
word = ''.join(letter for letter in word if letter.isalnum())
word_list = list(word.lower())
lengthList = len(word_list)
palindromo = int(lengthList/2) + 1)

if lengthList % 2 == 0:
    print('Não é um palídromo!')
else:
    for i in range(int(lengthList/2)):
        lengthList = lengthList - 1
        if word_list[i] == word_list[lengthList]:
            if (palindromo == (i+2)):
                print('É um palídromo!')
        else:
            print('Não é um palídromo!')
            break