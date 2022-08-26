import random

number = 3
"""
Şöyle bir şey yapıcaz
Sayı n ise 2*n kadar sayı yazıcaz ve bu sayıların yarısı 0 diğer yarısı 1 olucak. 1 olmadan 0 olmıycak.
Sonrasında 0 olan yere ')' 1 olan yere '(' koyucaz
"""

number_list = []
number_list.append(1)

for i in range(2*number):
    if number_list.count(1) < number_list.count(0):
        number_list.append(1)
    else:
        if number_list.count(1) <  number:
            if random.randint(0,1) == 0:
                number_list.append(0)
            else:
                number_list.append(1)


        else:
            for i in range(2*number-len(number_list)):
                number_list.append(0)
print(number_list)