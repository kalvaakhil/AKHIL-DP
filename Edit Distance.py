    #https://practice.geeksforgeeks.org/problems/edit-distance3702/1?page=2&difficulty[]=1&curated[]=1&sortBy=submissions
  def editDistance(self,word1,word2):
        M = len(word1)
        N = len(word2)
        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]
        for j in range(N, -1, -1):
            dp[M][j] = N - j
        for i in range(M, -1, -1):
            dp[i][N] = M - i
        # print(dp)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                    continue
                dp[i][j] = 1+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        return dp[0][0]
