class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()


        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R: 
                sum = val + nums[L] + nums[R]
                if sum < 0: 
                    L += 1
                elif sum > 0: 
                    R -= 1
                else:
                    res.append([val, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return res
                
            