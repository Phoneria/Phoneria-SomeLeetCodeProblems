heights = [2,1,5,6,2,3,7,8,9,5,3,1]
"""
Amacımız bu sütuna değen ve sütundan büyük tüm sütunları tek bir listede toplamak
"""
values = heights.copy()

for i in range(len(heights)):
    temp_list = []

    for j in range(i,len(heights)):
        if (heights[i]<=heights[j]):
            temp_list.append(heights[j])


        else:
            break
    for k in range(i-1,0,-1):
        if heights[i]<=heights[k]:
            temp_list.append(heights[k])

        else:
            break


    values.append(len(temp_list)*heights[i])

print(max(values))