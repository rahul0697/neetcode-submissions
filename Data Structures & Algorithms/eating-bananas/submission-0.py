class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        n = len(piles)
        low = 1
        high = piles[n-1]
        res = piles[n-1]
        while(low<=high):
            k = (low+high)//2
            cnt = 0
            for i in range(len(piles)):
                cnt = cnt + math.ceil(piles[i]/k)
            # res = min(cnt, res)
            if cnt<=h:
                high = k-1
                res = k
            else:
                low=k+1
        return res

            