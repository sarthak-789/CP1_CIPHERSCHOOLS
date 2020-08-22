# link: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        i=0
        while i<len(s):
            s1=dict[s[i]]
            if i+1<len(s):
                s2=dict[s[i+1]]
                if s1>=s2:
                    result+=s1
                    i+=1
                else:
                    result+=s2-s1
                    i+=2
            else:
                result+=s1
                i+=1
        return result
            
        