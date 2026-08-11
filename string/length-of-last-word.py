class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = list(s)
        count = 0
        last_word = len(L) - 1
        if last_word == 0:
            return 1

        for i in range(last_word, -1, -1):
            if L[i] == ' ' and count == 0: 
                continue
            elif L[i] != ' ':
                count += 1
            else:
                break

        return count