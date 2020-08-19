# link: https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        l=nums[:n]
        l1=nums[n:]
        for i in range(n):
            result.append(l[i])
            result.append(l1[i])
        return result