class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor= 0
        for i in range(len(nums)):
            xor = xor^i
            xor = xor^nums[i]

        xor = xor ^ len(nums)
        return xor