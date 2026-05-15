class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def checkanagram(s, t):
            if len(s)!=len(t):
                return False
            else:
                checks={}
                checkt={}
                for i in range(len(s)):
                    checks[s[i]] = 1 + checks.get(s[i],0)
                    checkt[t[i]] = 1 + checkt.get(t[i],0)
                return checks==checkt

        ha = {}
        result = []
        for i in range(len(strs)):
            if strs[i] not in ha:
                output=[]
                
                ha[strs[i]]=True
                output.append(strs[i])
                for j in range(i+1, len(strs)):
                    if checkanagram(strs[i], strs[j]):
                        output.append(strs[j])
                        ha[strs[j]]=True
                result.append(output)


        return result
                

        

