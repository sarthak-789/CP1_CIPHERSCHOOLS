# link : https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dict:
                sums = dict[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dict[value] = i
        return maxlength