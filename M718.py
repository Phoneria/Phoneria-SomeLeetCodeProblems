#Maximum Length of Repeated Subarray

nums1 = [0,0,0,0,0,0]
nums2 = [0,0,0,0,0,0]

common= []

for i in nums1:
    if i in nums2:
        nums2.remove(i)
        common.append(i)

print(common)