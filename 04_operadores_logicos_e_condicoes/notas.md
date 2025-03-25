#x = True
#y = True
#z = False

#x or y and z #--> True

#(x or y) and z #--> False


x = input('Seu ano de nascimento: ')

if int(x) % 4 == 0:
    print('Seu ano de nascimento é bissexto')
else:
    print('Seu ano não é bissexto')