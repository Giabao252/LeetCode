class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer
        clean_s = [c.lower() for c in s if c.isalnum()]
        i = 0
        j = len(clean_s) - 1

        if clean_s == []:
            return True

        while i <= j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
            

        return True


        