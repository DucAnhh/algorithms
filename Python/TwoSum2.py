class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while(left < right):
            total = numbers[left] + numbers[right]
            if total < target:
                left = left + 1
            elif total > target:
                right = right - 1
            else:
                return [left + 1, right + 1]