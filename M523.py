#Continuous Subarray Sum
"""
Create all sub arrays and collect all items in that array. If k is the divisor of the sum of the list return True

"""
nums = [23,2,4,6,7]
k = 13
def subsets(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output



def is_true(nums,k):
    for i in subsets(nums):
        if sum(i)!=0 and sum(i)%k==0 :
            return True
        return False

print(is_true(nums,k))