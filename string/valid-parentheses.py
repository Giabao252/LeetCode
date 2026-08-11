
class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        L = list(s)
        hashmap = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for i in L:
            if i in hashmap.values(): #if i is an opening bracket
                stack1.append(i) #push it to the stack
            elif i in hashmap.keys(): #if i is a closing bracket
                if len(stack1) == 0 or hashmap[i] != stack1.pop():
                    #Since the last bracket in the stack is expecting the first closing bracket
                    #if the popped bracket does not match the current closing bracket: FALSE
                    return False 
        return not stack1 #stack should be empty if all brackets matched

