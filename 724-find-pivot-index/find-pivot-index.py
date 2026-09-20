class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left=0
        tot=0
        for i in range(len(nums)):
            tot+=nums[i]
        leftsum=0
        rightsum=0
        for i in range(len(nums)):
            rightsum=tot-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1