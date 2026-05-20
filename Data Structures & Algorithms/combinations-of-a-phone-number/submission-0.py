class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

        if digits=="":
            return []
        ans = []
        def dfs(i, l , res):

            if i==len(l)-1:
                ans.append(res)
                return
            if i+1<len(l):
                for j in range(len(l[i+1])):
                    res = res+l[i+1][j]
                    dfs(i+1, l, res)
                    res = res[:-1]
                
        
        
        
        l = []
        for digit in digits:
            l.append(d[digit])

        for c in l[0]:
            dfs(0, l,c)
        return ans