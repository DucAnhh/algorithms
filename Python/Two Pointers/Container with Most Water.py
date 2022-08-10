class Solution:
    def maxArea(self, height) -> int:
        answer = 0
        
        l, r = 0, len(height) - 1
        
        while l < r:
            newArea = (r-l)*min(height[l], height[r])
            if newArea > answer:
                answer =  newArea
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
            
        return answer

height = [2, 3, 4, 5, 18, 17, 6]
a = Solution()
print(a.maxArea(height))