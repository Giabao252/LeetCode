class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            number_str = str(i)
            is_self_dividing = True

            for ch in number_str:
                if ch == '0':
                    is_self_dividing = False
                    break
                digit = int(ch)
                if i % digit != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                res.append(i)

        return res