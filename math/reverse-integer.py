class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = (x > 0) - (x < 0)  # Extracting the sign of x
        x = abs(x)  # Working with the absolute value

        arr = list(map(int, str(x)))
        arr1 = []

        for i in range(len(arr)):
            arr1.append(arr.pop())

        reversed_x = sign * int("".join(map(str, arr1)))
        if reversed_x >= 2**31 - 1 or reversed_x <= -2**31:
            return 0

        return reversed_x
