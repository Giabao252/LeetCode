from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:k])

        if window_count == s1_count:
            return True

        for i in range(k, len(s2)):
            left_char = s2[i - k]
            right_char = s2[i]

            window_count[right_char] += 1
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            if window_count == s1_count:
                return True

        return False