class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write in chars
        read = 0   # Position to read from chars
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count consecutive occurrences
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if > 1
            if count > 1:
                # Convert count to string and write each digit
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write  # New length of compressed 
        
        #TIME: O(N) - just 1 iteration through the array
        #SPACE: O(1) - modified the array in place