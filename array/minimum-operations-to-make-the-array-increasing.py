class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1 - nums[i]
                ops += needed
                nums[i] += needed 

        return ops