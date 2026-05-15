class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = dict()
        for num in nums:
            if num in h.keys():
                return True
            else:
                h[num]=1
        return False
        