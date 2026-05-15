class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for num in nums:
            if num in s:
                return True;
            else:
                s[num]=True
        return False