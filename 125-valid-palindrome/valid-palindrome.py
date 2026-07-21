class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=''
        for i in s:
            if i.isalnum():
                st+=i
        left=0
        right=len(st)-1
        while(left<right):
            if st[left]!=st[right]:
                return False
            left+=1
            right-=1
        return True
        