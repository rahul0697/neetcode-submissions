class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = dict()
        for st in strs:
            sort = " ".join(sorted(st))
            if sort in ss:
                ss[sort].append(st)
            else:
                ss[sort]=[st]

        return list(ss.values())        