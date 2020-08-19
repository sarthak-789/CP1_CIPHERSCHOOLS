#https://leetcode.com/problems/fibonacci-number/
# using benet's Formulae

class Solution:
    def fib(self, N: int) -> int:
        r= (1+5**0.5)/2
        return int((r**N +1 )/(5**0.5))
        