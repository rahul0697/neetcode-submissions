class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        visited = [0]*len(nums)
        res = [[]]
        def dfs(i, nums,ans):
            
            ans.append(nums[i])
            print(ans)
            res.append(ans.copy())
            for j in range(i+1, len(nums)):
                dfs(j, nums, ans)

            ans.pop()        


        for i in range(len(nums)):
            dfs(i, nums, [])
        return res