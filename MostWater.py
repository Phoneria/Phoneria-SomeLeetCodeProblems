height = [1,8,6,2,5,4,8,3,7]

volume = []

for i in height:
    for j in height:
        min_height = j
        if i < j :
            min_height =i

        max_volume = min_height * abs(height.index(i)-height.index(j))


        volume.append(max_volume)
max_water = max(volume)
print(max_water)
