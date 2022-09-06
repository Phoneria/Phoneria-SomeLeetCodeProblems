# Subarray Sum Equals K
def subsets(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

nums = [1,2,3]
k = 3
a = 0
for i in subsets(nums):
    if sum(i) == k:
        a +=1
print(a)