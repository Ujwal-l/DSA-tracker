class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        sign = -1 if x<0 else 1
        x=abs(x)
        while x>0:
            reverse = reverse*10 + x%10
            x//=10
        reverse*=sign

        return reverse if -2**31<=reverse<=2**31 else 0
        