class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointer
        container = 0
        i = 0
        j = len(height) - 1

        while i < j:
            curr_container = (j-i)*min(height[i], height[j])
            if curr_container > container: 
                container = curr_container
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return container
