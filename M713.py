# Subarray Product Less Than K

nums = [10,5,2,6]

k = 100

def subsets(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

product=[]

for i in subsets(nums):
    prd= 1
    for j in i:
        prd*=j
    if prd<k:
        product.append(i)

print(product)
