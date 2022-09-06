#Kth Smallest Number in Multiplication Table
import numpy as np


def kth_element(m,n,k):
    mltp_list= np.arange(m*n).reshape(m,n)

    for i in range(m):
        mltp_list[i][0] = i+1

    for i in range(n):
        mltp_list[0][i]= i+1

    for i in range(len(mltp_list)):
        for j in range(len(mltp_list[0])):
            mltp_list[i][j]= mltp_list[0][j]*mltp_list[i][0]


    one_d = []

    for i in mltp_list:
        for j in i:
            one_d.append(j)

    one_d.sort()
    print(one_d)
    return(one_d[k-1])

print(kth_element(3,3,5))