import string
import re

print('Identificando a quantidade de palavras!')


phrase = input('\nDigite sua frase: ')
list_words = re.findall(r"[\w]+", phrase)

print('List Word -> ', list_words)

print('O texto contém ', len(list_words), ' palavras.')