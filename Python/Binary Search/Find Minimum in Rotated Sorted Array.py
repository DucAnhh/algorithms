from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while (l<=r):
            if(r==l+1): # when we have only two elements
                return min(nums[l], nums[r])
            elif r==l: # when we have one elements
                return nums[l]
            else:
                m = (l+r)//2
                
            if(nums[m] >= nums[l]):
                if nums[m] >= nums[r]: 
                    l = m 
                else:
                    r = m
            else:
                r = m

a = Solution()
nums = [4,5,6,7,0,1,2]
print(a.findMin(nums))