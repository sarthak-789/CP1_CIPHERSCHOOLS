#link: https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            k=1
            l=[]
            for j in range(i+1):
                l.append(k)
                k=int(k*((i+1)-(j+1))/(j+1))
            result.append(l)
        return result
            