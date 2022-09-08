from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search a target in a "possibly rotated" array
        l = 0
        r = len(nums) - 1
        while (l<=r):
            m = l + ((r - l) // 2)
            # immediately found target
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            # easiest case: nums[m] > nums[l]
            if nums[m] >= nums[l] and target >= nums[l] and nums[m] > target:
                # example: nums = [4, 5, 6, 7, 8, 1, 2], target = 5
                # so, in the first interval, we have nums[m] = 7 and target will be in subarray [4, 5, 6]
                r = m - 1
            elif nums[m] >= nums[l] and target >= nums[l] and nums[m] < target: 
                # example: nums = [4, 5, 6, 7, 8, 1, 2], target = 8
                l = m + 1
            elif nums[m] >= nums[l] and target <= nums[l] and nums[m] > target:
                # example: nums =  [4, 5, 6, 7, 8, 1, 2], target = 1
                l = m + 1
                
                
            # harder case: nums[m] < nums[l]
            elif nums[m] <= nums[l] and target <= nums[l] and nums[m] < target:
                # example: nums = [5, 6, 0, 1, 2, 3, 4], target =  3
                l = m + 1
            elif nums[m] <= nums[l] and target <= nums[l] and nums[m] > target:
                # example: nums = [5, 6, 0, 1, 2, 3, 4], target =  0
                r = m - 1
            elif nums[m] <= nums[l] and target >= nums[l] and nums[m] < target:
                # example: nums = [5, 6, 0, 1, 2, 3, 4], target =  6
                r = m - 1
        return -1

a = Solution()
nums = [4,5,6,7,0,1,2]
target = 3
print(a.search(nums, target))