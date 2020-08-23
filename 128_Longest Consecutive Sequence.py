# link : https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                n=num
                current = 1

                while n + 1 in num_set:
                    n += 1
                    current += 1

                result = max(result, current)

        return result