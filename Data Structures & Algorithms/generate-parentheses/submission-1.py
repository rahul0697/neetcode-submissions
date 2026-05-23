class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        m = 2*n
        o = '('
        c = ')'

        ans = []
        def dfs(i, res, op, cl):

            if op>n or cl>n or cl>op:
                return
            if i==m:
                ans.append(res)
                return
            
            dfs(i+1, res+o, op+1, cl)
            dfs(i+1, res+c, op, cl+1)




        dfs(0, '', 0, 0)
        return ans



