my_dict ={'I' : 1 ,
          "V" : 5,
          "X" : 10,
          "L": 50,
          "C" : 100,
          "D": 500,
          "M": 1000
          }


number = input("Number : ")

result = 0

number =number[::-1]




for i in range(len(number)):
    if i == 0:

        result += my_dict[number[i]]
    else :

        if my_dict[number[i]] < my_dict[number[i-1]]:

            result -= my_dict[number[i]]
        else:
            result += my_dict[number[i]]

print(result)