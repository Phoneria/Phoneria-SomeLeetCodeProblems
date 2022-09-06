#Find K-th Smallest Pair Distance

nums = [1,6,1]

k = 3
def distance(nums,k):
    nums.sort()
    dst= []

    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if j!=i:

                dst.append(abs(nums[i]-nums[j]))
    return(dst[k-1])

