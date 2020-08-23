# link : https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    l=[]
    def tribonacci(self, n: int) -> int:
        self.l=[0,1,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        for i in range(3,n+1):
            self.l.append(self.l[i-3]+self.l[i-2]+self.l[i-1])
        
        return self.l[-1]