from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can use th algorithm with twice binary search like video solution
        # but the below code (my first idea) is shorter
        arr = [] # arr is the union of all subarray in matrix
        for i in matrix:
            arr =  arr + i
        l = 0
        r =  len(arr)-1
        
        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
a = Solution()
print(a.searchMatrix(matrix, target))