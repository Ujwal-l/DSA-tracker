class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest =0 
        mySet = set(nums)
        for c in mySet:
            if c-1 not in mySet:
                length = 1
                while c + length in mySet:
                    length +=1
                longest=max(longest,length)
        return longest
