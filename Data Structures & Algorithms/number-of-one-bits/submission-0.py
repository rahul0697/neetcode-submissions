class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while(n):
            # print(n)
            rem = n%2
            if rem==1:
                cnt+=1
            n = int(n/2)

        return cnt