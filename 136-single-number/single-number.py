class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp={}
        for i in nums:
            temp[i]=temp.get(i,0)+1
        for i in temp:
            if temp[i]==1:
                return i