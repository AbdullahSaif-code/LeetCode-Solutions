class Solution:
    def romanToInt(self, s: str) -> int:
        I,V,X,L,C,D,M = 1,5,10,50,100,500,1000
        roman = {'I':I,'V':V,'X':X,'L':L,'C':C,'D':D,'M':M}
        num = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num
sol = Solution()
print(sol.romanToInt("III"))