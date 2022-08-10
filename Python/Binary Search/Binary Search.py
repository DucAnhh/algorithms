# Bisection
class Solution1:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

# 0(log n) complexity
class Solution2:
    def search(self, nums, target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
        return -1