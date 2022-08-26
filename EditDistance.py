word1="horse"
word2= "rose"

dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
for i in range(len(word1)+1):
    print("Önce : ",i,dp)

    dp[i][0] = i
    print("Sonra :" ,i,dp)
    for j in range(1,len(word2)+1):
        if i == 0:
            dp[0][j] = j
        elif word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

print(dp[-1][-1] )
