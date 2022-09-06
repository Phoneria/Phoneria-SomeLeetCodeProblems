# Shortest Unsorted Continuous Subarray

nums = [2,6,4,8,10,9,15]

def min_sub ( array ):
    sorted_array =sorted(array)
    print(sorted_array)
    print(array)
    if sorted_array == array:
        return 0

    first_index = 0
    last_index = 0
    for i in range(len(sorted_array)):

        if sorted_array[i] != array[i]:

            first_index = i
            break


    for i in range(len(nums)-1,0,-1):
        if sorted_array[i]!=array[i]:

            last_index= i
            break



    sub_list = []

    print(first_index)
    print(last_index)

    for i in range(first_index,last_index+1):
        sub_list.append(array[i])

    return sub_list


print(min_sub(nums))

