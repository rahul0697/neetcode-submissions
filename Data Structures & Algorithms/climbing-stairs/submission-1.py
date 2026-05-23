class Solution:
    def climbStairs(self, n: int) -> int:
        
        t = [0]*(n+1)
        def knapsack(n):
            if n<0:
                return 0
            if(n==0):
                return 1

            if t[n]!=0:
                return t[n]

            t[n] = knapsack(n-1)+knapsack(n-2)
            return t[n]


        return knapsack(n)

