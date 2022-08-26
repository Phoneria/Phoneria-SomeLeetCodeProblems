strs = ["eat","tea","tan","ate","nat","bat"]


grouped =[]

for i in strs:
    temp = []
    for j in i:
        temp.append(j)
    temp.sort()
    grouped.append(temp)
grouped.sort()
print(grouped)