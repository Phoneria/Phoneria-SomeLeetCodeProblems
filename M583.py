#Delete Operation for Two Strings

word1 = "leetcode"
word2 = "etco"


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)



    def lcs(i, j):  # find longest common subsequence
        if i == m or j == n:
            return 0
        return 1 + lcs(i + 1, j + 1) if word1[i] == word2[j] else max(lcs(i + 1, j), lcs(i, j + 1))
        # subtract the lcs length from both the strings

    # the difference is the number of characters that has to deleted
    return m + n - 2 * lcs(0, 0)

print(minDistance(word1,word2))