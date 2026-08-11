class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bin = []

        for i in nums:
            if i not in bin:
                bin.append(i)
            else:
                bin.remove(i)
        
        if len(bin) != 0: 
            return bin[0]