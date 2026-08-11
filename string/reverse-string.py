class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0 
        ptr2 = len(s) - 1
        temp = ""

        while ptr1 < ptr2:
            temp = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = temp
            ptr1 += 1
            ptr2 -= 1