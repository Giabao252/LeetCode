class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i in numSet: #iterate through set is faster than through list
            if (i - 1) not in numSet: 
                length = i + 1 #start of sequence identified
                while length in numSet:
                    length += 1
                longest = max(longest, length - i)        
        return longest
