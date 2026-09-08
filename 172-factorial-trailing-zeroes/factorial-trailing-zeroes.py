class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        i=1
        while (n//(5**i))>0:
            ans+=(n//(5**i))
            i+=1
        return ans