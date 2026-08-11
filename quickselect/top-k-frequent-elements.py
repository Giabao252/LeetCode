class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        # Count frequencies
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Create list of [frequency, number] pairs
        freq_list = []
        for number in hashmap:
            frequency = hashmap[number]
            freq_list.append([frequency, number])
        
        # Sort by frequency (first element)
        freq_list.sort(reverse=True)
        
        # Build result with top k numbers
        result = []
        for i in range(k):
            number = freq_list[i][1]  # Get the number (second element)
            result.append(number)
        
        return result