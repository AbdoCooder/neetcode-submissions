class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l = 0
        lenght = len(nums)
        for i in range(lenght):
            if l == total - l - nums[i]:
                return i
            l += nums[i]
        return -1
