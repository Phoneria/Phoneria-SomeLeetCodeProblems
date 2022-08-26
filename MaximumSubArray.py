nums = [-2,1,-3,4,-1,2,1,-5,4]


tempSum = maxSum = nums[0]


for num in nums[1:]:
    tempSum = max(num, tempSum + num)
    maxSum = max(maxSum, tempSum)

print(maxSum)
