class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [0]*len(nums)

        def dfs(i, nums, res):

            
            if len(res)==len(nums):
                ans.append(res.copy())
                return

            
            for j in range(len(nums)):
                if visited[j]==0:
                    visited[j]=1
                    res.append(nums[j])
                    dfs(j, nums, res)
                    res.pop()
                    visited[j]=0
            


        for i in range(len(nums)):
            visited[i]=1
            dfs(i, nums, [nums[i]])
            visited[i]=0

        return ans