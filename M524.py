#Longest Word in Dictionary through Deleting
"""
Scan each word and delete them if they have extra letter from s. And then return the max length element of list
"""

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]

def longest(s,d):
    for word in d:
        is_there = True
        for letter in word:

            if not letter in s:
                is_there = False

        if not is_there:
            d.remove(word)
    max_long =" "
    for i in d:
        if len(i) > len(max_long):
            max_long = i

    return max_long

print(longest(s,dictionary))