nums = [100,4,200,1,3,2]


nums = sorted(nums)

print(nums)


max = 1

for i in range(len(nums)-1):
    if nums[i+1] == nums[i]+1:
        max+=1


print(max)