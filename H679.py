# 24 Game
from itertools import combinations


cards = [4,1,8,7]

all_cmb= list(combinations(cards,2))


def generate_num (a,b):
    all_list=[]
    if a< b:
        c = a
        a =b
        b =c

    all_list.append(a*b)
    all_list.append(a * b)
    all_list.append(a - b)
    if b!=0:
        all_list.append(a / b)

    return (all_list)
is_true=False

for i in range(int(len(all_cmb)/2)):

    a = generate_num(all_cmb[i][0],all_cmb[i][1])
    b= generate_num(all_cmb[-i][0],all_cmb[-i][1])

    for number in range(len(a)):
        result = generate_num(a[number],b[number])
        print(result)
        if 24 in result:
            is_true= True
print(is_true)
