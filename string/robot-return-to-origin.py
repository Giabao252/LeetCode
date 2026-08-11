class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U = 0
        D = 0
        L = 0
        R = 0

        for i in moves:
            if i == 'U':
                D += 1
            elif i == 'D':
                U += 1
            elif i == 'L':
                R += 1
            elif i == 'R':
                L += 1
        
        if (U != D) or (L != R):
            return False
        return True