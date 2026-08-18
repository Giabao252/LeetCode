class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            mid = (low + high) // 2

            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            
            if numbers[low] + numbers[mid] == target:
                return [low + 1, mid + 1]

            if numbers[high] + numbers[mid] == target:
                return [mid + 1, high + 1]
            
            elif numbers[low] + numbers[mid] < target: 
                low = mid + 1
            elif numbers [mid] + numbers[high] > target:
                high = mid -1
        
        return -1