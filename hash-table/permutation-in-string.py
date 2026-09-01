class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation = list(s1)
        permutation.sort()
        k = len(s1)

        for i in range(len(s2) - k):
            temp = [s2[i], s2[i+1]]
            temp.sort()
            if temp == permutation:
                return True
            
        return False