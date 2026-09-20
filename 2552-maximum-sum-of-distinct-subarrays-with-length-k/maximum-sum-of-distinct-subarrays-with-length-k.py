class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l=set()
        s=0
        m=0
        i=0
        for j in range(len(nums)):
            while nums[j] in l:
                l.remove(nums[i])
                s-=nums[i]
                i+=1
            l.add(nums[j])
            s+=nums[j]
            if j-i+1>k:
                l.remove(nums[i])
                s-=nums[i]
                i+=1
            if j-i+1==k:
                m=max(s,m)
        return m
