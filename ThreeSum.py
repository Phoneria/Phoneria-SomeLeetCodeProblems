nums = [-1,0,1,2,-1,-4]
list = []

for first in range(len(nums)):
    for second in range(len(nums)):
        if nums[first]!= nums[second]:

            other_one=-( nums[first] + nums[second])

            if other_one in nums and nums.index(other_one)!=nums.index(nums[first]) and nums.index(other_one)!=nums.index(nums[second]):
                temp = []
                maks_num = max(nums[first],nums[second],-( nums[first] + nums[second]))
                min_num = min(nums[first],nums[second],-( nums[first] + nums[second]))
                other_one=-( maks_num + min_num )

                temp.append(maks_num)
                temp.append(other_one)
                temp.append(min_num )

                list.append(temp)

set_list = []

for i in list:
    if not i in set_list:
        set_list.append(i)
print(set_list)


