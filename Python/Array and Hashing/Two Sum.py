class Solution:
    def twoSum(self, nums, target: int):
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

a = Solution()
a.twoSum([1, 4, 5, 2], 9)