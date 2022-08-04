from dataclasses import dataclass
@dataclass
class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

a = Solution()
print(a.containsDuplicate([1,2,3,1]))
print(a.containsDuplicate([1,2,4,5]))