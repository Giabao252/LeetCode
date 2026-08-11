class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        hashmap = {}

        for i in magazine:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for i in ransomNote: 
            if i in hashmap and hashmap[i] == 0:
                return False
            elif i in hashmap: 
                hashmap[i] -= 1
            elif i not in hashmap:
                return False

        return True 
