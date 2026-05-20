class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

        if digits=="":
            return []
        ans = []
        def dfs(i, res):

            if i==len(digits):
                ans.append(res)
                return 

            for c in d[digits[i]]:
                dfs(i+1, res+c)


        dfs(0, "")
        return ans