class Solution:
    def isHappy(self, n: int) -> bool:
        
        def func(n): 
            s = 0
            while(n):
                rem = n%10
                n = int(n/10)
                s = s + rem*rem
            return s

                    
        ss = set()
        while(True):
            n = func(n)
            if n==1:
                return True
            if n in ss:
                return False
            else:
                ss.add(n)