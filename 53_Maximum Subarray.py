# link : https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=0
        res=-2**31
        for i in nums:
            mx=mx+i
            res=max(res,mx)
            if mx<0:
                mx=0            
        return res