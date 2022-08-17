from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == "*" :
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]

tokens = ["2","1","+","3","*"]
a = Solution()
print(a.evalRPN(tokens))