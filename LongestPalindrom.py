word = input("Word : ")

word_list = []
palindrom_list = []


for i in range(len(word)):
    letter =word[i]

    for j in range(len(word)-1,0,-1):

        if word[j] == word[i]:
            str = ""
            for h in range(i,j+1) :
                str +=word[h]

            if str != "" and ((len(str) != 1) and (len(str) != 2)) :
                word_list.append(str)




def isPalindrome(s):
    return s == s[::-1]

for element in word_list:
    if isPalindrome(element):
        palindrom_list.append(element)

longest_palindrome = ""
for i in palindrom_list:
    if len(i) > len(longest_palindrome):
        longest_palindrome = i


print(longest_palindrome)


