class Solution:
    def threeSum(self, nums):
        answer = []
        hashset =[]
        
        # Common idea: O(n^3) complexity
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if {nums[i], nums[j], nums[k]} not in hashset:
        #                     answer.append([nums[i], nums[j], nums[k]])
        #                     hashset.append({nums[i], nums[j], nums[k]})
        
        # Using sort so O(n^2) complexity
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    if {nums[i], nums[l], nums[r]} not in hashset:
                        answer.append([nums[i], nums[l], nums[r]])
                        hashset.append({nums[i], nums[l], nums[r]})
                    l += 1
        
        return answer

nums = [-1,0,1,2,-1,-4]
a = Solution()
print(a.threeSum(nums))