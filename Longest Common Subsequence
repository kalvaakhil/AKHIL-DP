#https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        akhildp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if(text1[i]==text2[j]):
                    akhildp[i][j]=1+akhildp[i+1][j+1]
                else:
                    akhildp[i][j]=max(akhildp[i][j+1],akhildp[i+1][j])
        return akhildp[0][0]
