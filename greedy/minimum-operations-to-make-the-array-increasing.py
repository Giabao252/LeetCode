class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i] < nums[j]:
                    continue
                elif nums[i] == nums[j]:
                    nums[j] += 1
                    ops += 1
                else: 
                    while nums[i] >= nums[j]:
                        nums[j] += 1
                        ops += 1
        return ops
