class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ss= dict()
        for i in range(len(nums)):
            if target-nums[i] in ss:
                return [ss[target-nums[i]],i]
            
            ss[nums[i]]=i
