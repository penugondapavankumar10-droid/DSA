class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        minle=float('inf')
        cursum=0
        for right in range(len(nums)):
            cursum+=nums[right]
            while cursum>=target:
                if right-left+1<minle:
                    minle=right-left+1
                cursum-=nums[left]
                left+=1
        if minle==float('inf'):
            return 0
        else:
            return minle