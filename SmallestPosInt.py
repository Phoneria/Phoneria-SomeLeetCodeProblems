nums = [7,8,9,11,12]


for i in range(len(nums)):
    if not i in nums and i>0:
        print(i)
        break
