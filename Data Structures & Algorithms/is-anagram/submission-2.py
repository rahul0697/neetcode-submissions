class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = " ".join(sorted(s))
        tt = " ".join(sorted(t))
        if ss==tt:
            return True
        return False 