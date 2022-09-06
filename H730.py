# Count Different Palindromic Subsequences


s = "bccb"
def number_of_palindrome(s):
    def subsets(nums):
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


    def is_palindrome (s):
        is_p=True
        for i in range(len(s)):

            if s[i]!=s[-i-1]:
                is_p = False
        return is_p

    all_p = []

    for i in subsets(s):
        if is_palindrome(i):
            if not i in all_p:
                all_p.append(i)

    return(len(all_p)-1)

