class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = {}
        res2 = {}

        for ch in s:
            if ch in res1:
                res1[ch]=res1[ch]+1
            else:
                res1[ch]=1
            
        for ch in t:
            if ch in res2:
                res2[ch]=res2[ch]+1
            else:
                res2[ch]=1

                
        return res1==res2
        