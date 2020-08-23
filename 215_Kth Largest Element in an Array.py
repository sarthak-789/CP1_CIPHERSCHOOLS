# link : https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k or len(nums)==0:
            return -1
        nums.sort()
        return nums[-k]