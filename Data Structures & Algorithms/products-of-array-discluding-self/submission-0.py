class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        j = len(nums)-2
        while(j>=0):
            suffix[j]= suffix[j+1]*nums[j+1]
            j = j-1
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]

        return res