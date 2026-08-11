class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        counter = 1
        answer = list()

        while counter <= n:
            if (counter % 5 == 0) and (counter % 3 == 0):
                answer.append("FizzBuzz")
            elif counter % 3 == 0:
                answer.append("Fizz")
            elif counter % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(counter))
            counter += 1
        
        return answer