#https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1?page=5&curated[]=1&sortBy=submissions
class Solution:
	def lps(self, s):
	    n=len(s)
        le=0
        lps=[0]*n
        i=1
        while i<n:
            if s[i]==s[le]:
                le+=1
                lps[i]=le
                i+=1
            else:
                if le!=0:
                    le=lps[le-1]
                else:
                    lps[i]=0
                    i+=1
        return lps[n-1]
