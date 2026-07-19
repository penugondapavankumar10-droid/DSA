class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            else:
                count+=1
        for i in range(n-count,n):
            nums[i]=0