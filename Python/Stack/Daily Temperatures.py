from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]: # if find a warmer day
                ele = stack.pop() # get the top element in stack
                ans[ele[0]] = i - ele[0] # calculate the number day to wait
            # push the present day to stack
            stack.append([i, temp])
        return ans

temperatures = [73,74,75,71,69,72,76,73]
a = Solution()
print(a.dailyTemperatures(temperatures))