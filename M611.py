# Valid Triangle Number

nums = [2,2,3,4]

def is_triangle(a,b,c,):

    if a+b >c and a+c>b and  b+c > a :
        return True
    return False

def subsets(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

triangles= 0
for i in subsets(nums):
    if len(i) == 3:
        if is_triangle(i[0],i[1],i[2]):
            triangles+=1
print(triangles)

