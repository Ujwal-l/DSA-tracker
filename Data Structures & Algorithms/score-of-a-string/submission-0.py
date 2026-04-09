class Solution:
    def scoreOfString(self, s: str) -> int:
        count=0
        for i in range(1,len(s)):
            if ord(s[i]) > ord(s[i-1]):
                count+=ord(s[i])-ord(s[i-1])
            else:
                count+=ord(s[i-1])-ord(s[i])
        return count

        