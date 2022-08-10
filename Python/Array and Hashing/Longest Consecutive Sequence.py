class Solution:
    def longestConsecutive(self, nums) -> int:
        # sort the array nums
        nums.sort()
        answer = 0 # returned answer
        count = 1 # count tạm thời
        
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]: # if the next element is same then continue
                i = i + 1
                continue
            if nums[i+1] - nums[i] == 1: # if the next element is consecutive with the present element
                count = count + 1 # then count + 1
            else:
                answer = max(answer, count) # else the sequence is end and count again
                count = 1
            i = i + 1
        answer = max(answer, count)
        return answer

nums = [0,3,7,2,5,8,4,6,0,1]
a = Solution()
print(a.longestConsecutive(nums))
