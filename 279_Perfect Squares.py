# link : https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=1
        # dp[2]=2
        for i in range(0,n+1):
            dp[i]=i
            j=1
            while(j*j <= i ):
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        return dp[n]