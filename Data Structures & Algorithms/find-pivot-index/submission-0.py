class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lenght = len(nums)

        prefix = [0] * lenght
        for i in range(lenght):
            if i == 0:
                prefix[i] = 0
            else:
                prefix[i] = prefix[i-1] + nums[i-1]
        
        postfix = [0] * lenght
        for i in range(lenght - 1, -1, -1):
            if i == lenght - 1:
                postfix[i] = 0
            else:
                postfix[i] = postfix[i+1] + nums[i+1]

        for i in range(lenght):
            if prefix[i] == postfix[i]:
                return i

        return -1
