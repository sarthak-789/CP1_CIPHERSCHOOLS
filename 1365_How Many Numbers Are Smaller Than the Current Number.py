# link : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            l.append(count)
        return l
        