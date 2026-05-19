class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ans = []
        def dfs(i, nums, s, res):

            if s==target:
                ans.append(res.copy())
                # print(s, ans)
                return
            elif s>target:
                return
            
            for j in range(i, len(nums)):
                res.append(nums[j])
                dfs(j, nums, s+nums[j], res)
                res.pop()

        dfs(0, nums, 0, [])

        return ans