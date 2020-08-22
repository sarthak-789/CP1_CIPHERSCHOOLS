# link : https://leetcode.com/problems/basic-calculator-ii/

import re
class Solution:
    def calculate(self, s: str) -> int:
        j=0
        l=[]
        s=s.replace(" ","")
        l=re.split('([+\-*/])',s)
        
        i = 0
        while i < len(l):
            if l[i] in '*/':
                operator = l[i]
                a = int(l.pop(i-1))
                l.pop(i-1)
                b = int(l.pop(i-1))
                if operator == '*':
                    l.insert(i-1, a*b)
                else:
                    l.insert(i-1, int(a/b))
                i-=1
            i+=1
        
        if len(l) == 1: return l[0]
        sum = int(l[0])
        i=1
        while i<len(l):
            operator = l[i]
            if operator == '+':
                sum += int(l[i+1])
            elif operator == '-':
                sum -= int(l[i+1])
            i+=1
        return sum