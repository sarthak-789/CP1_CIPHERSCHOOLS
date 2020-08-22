# link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        l=[True]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies < m:
                l[i]=False
        return l