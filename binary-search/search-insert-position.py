class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        index = 0

        for i in range(len(nums)):
            if nums[i] == target:
                index = i
                found = True

        if not found:
            for i in range(len(nums)):
                if nums[i] <= target and (i == len(nums) - 1 or nums[i + 1] >= target):
                    index = i + 1

        return index
