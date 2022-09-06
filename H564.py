#Find the Closest Palindrome
import math


n = 123456789


def closest_min_pal(number) :

    len_n = int(math.log10(n))+1

    if len_n == 1:
        return n-1

    else:

        half = int(len_n/2)


        str_n = (str(n)[0:half])

        if len_n%2 == 0:

            return str_n + str_n[::-1]
        else:
            return str_n  + str(n)[len(str_n)] +str_n[::-1]


print(closest_min_pal(n))

