import random

aposta = []
same_num = 0
print('Gerando os números para apostar na Mega Sena!')

num = random.randint(1,60)
aposta.append(num)

while len(aposta) < 6:

    num = random.randint(1,60)

    tam_list = len(aposta)
    for i in range(len(aposta)):        
        if aposta[i] == num:
            break
        else:
            same_num = same_num + 1
    if same_num == tam_list:
        aposta.append(num)
        same_num = 0
        print(aposta)
            

print('Seus numerios são -> ', sorted(aposta))
