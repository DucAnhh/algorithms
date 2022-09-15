from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def addNode(self, arr : List):
        curr = self
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        add1 = 0 # add 1 to next when sum > 10 (have a carry)
        while l1 or l2 or add1: # loop when still have digit or a carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 if add1 == 0 else val1 + val2 + 1
            
            if val_sum >= 10:
                val_sum = val_sum - 10
                add1 = 1
            else:
                add1 = 0
            
            curr.next = ListNode(val_sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ans.next

arr1 = [9, 9, 9]
list1 = ListNode(arr1[0])
list1.addNode(arr1)

arr2 = [9]
list2 = ListNode(arr2[0])
list2.addNode(arr2)

# Solve
a = Solution()
ans = a.addTwoNumbers(list1, list2)
res = []
while(ans):
    res.append(ans.val)
    ans = ans.next
print(res)