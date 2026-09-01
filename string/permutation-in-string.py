class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation = list(s1)
        permutation.sort()
        k = len(s1)

        for i in range(len(s2) - k):
            temp = []
            count = 0
            while count != k:
                temp.append(s2[i + count])
                temp.sort()
                count += 1
            if temp == permutation:
                return True
            
        return False