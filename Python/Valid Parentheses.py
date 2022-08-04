class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(": ")", "[": "]", "{": "}"} 
        stack = []
        for i in s:
            if i in map:
                stack.append(i)
            elif (len(stack) != 0) and (map[stack[-1]] == i):
                stack.pop()
            else: # when (len(stack) != 0) or (map[stack[-1]] != i)
                return False
        
        # if (len(stack) != 0):
        #     return False
        # else:
        #     return True
        return not stack # another short way