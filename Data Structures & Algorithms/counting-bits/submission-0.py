class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(n):
            cnt = 0
            while(n):
                rem=n%2
                if rem==1:
                    cnt+=1
                n = int(n/2)
            return cnt

        ans = []
        for i in range(n+1):
            ans.append(count(i))
        return ans