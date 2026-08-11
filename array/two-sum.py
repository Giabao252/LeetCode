class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #val : index

        for index, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[n] = index


        
