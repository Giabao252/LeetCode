class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointer -> push the val elements to the back and update k
        k = 0
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] != val and nums[j] != val:
                k += 1
                i += 1
            elif nums[i] != val and nums[j] == val: 
                k += 1
                j -= 1
                i += 1
            elif nums[i] == val and nums[j] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                k += 1
                i += 1
                j -= 1
            else:
                j -= 1
            
        return k