from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {} #sorted key : anagrams

        #handling edge cases
        if len(strs) == 1 or len(strs) == 0:
            res.append(strs)
            return res

        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str not in hashmap:
                hashmap[sorted_str] = []
                hashmap[sorted_str].append(i)
            elif sorted_str in hashmap:
                hashmap[sorted_str].append(i)
        
        res = list(hashmap.values())

        return res
            

