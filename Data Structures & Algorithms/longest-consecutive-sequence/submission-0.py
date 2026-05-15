class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ss = set(nums)
        res = 0
        for num in nums:
            count = 0
            curr = num
            while curr in ss:
                curr=curr+1
                count=count+1
            if res<count:
                res=count
        return res
            