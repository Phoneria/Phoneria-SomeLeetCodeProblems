num = "1432219"
k = 3
num = num[3:]


e = []

for i in num :
    e.append(i)


e.sort()

print(e)

new_num = ""

for i in e:
    new_num+=i

print(new_num)