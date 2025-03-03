class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
x= 121
sol = Solution()
print(sol.isPalindrome(x))