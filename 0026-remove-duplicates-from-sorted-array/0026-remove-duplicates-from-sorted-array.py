class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
                continue
            i += 1
        return len(nums)
List = [1,1,2]
slo = Solution()
print(slo.removeDuplicates(List))  