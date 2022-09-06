#Reach a Number

def reachNumber( target):
    target = abs(target)
    k = 0
    while target > 0:
        k += 1
        target -= k
        print(k , target)
    return k if target % 2 == 0 else k + 1 + k % 2


print(reachNumber(9))