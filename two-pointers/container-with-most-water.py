class Solution:
    def maxArea(self, height: List[int]) -> int:
        container = 0
        i = 0
        j = len(height) - 1

        while i < j:
            curr_container = (j-i)*min(height[i], height[j])
            if curr_container > container: 
                container = curr_container
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return container
