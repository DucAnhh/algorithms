from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #based on intruction video 
        stack = []
        ans = []

        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                ans.append("".join(stack))
                return

            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClose)
                stack.pop()
            if numClose < numOpen:
                stack.append(")")
                backtrack(numOpen, numClose + 1)
                stack.pop()

        backtrack(0, 0)
        return ans

n = 3
a = Solution()
print(a.generateParenthesis(n))