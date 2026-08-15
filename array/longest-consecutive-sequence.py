class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i in numSet:
            if (i - 1) not in numSet: 
                length = i + 1
                while length in numSet:
                    length += 1
                longest = max(longest, length - i)        
        return longest
