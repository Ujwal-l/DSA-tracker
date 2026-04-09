class Solution:
    def isPalindrome(self, s: str) -> bool:
        k= [x.lower() for x in s if x.isalnum()]
        l=0
        r=len(k)-1
        while l<r:
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True
        