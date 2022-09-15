from typing import Optional, List
import numpy as np
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using twice reversions
        head = self.reverseList(head)
        prev, curr = None, head
        for i in range(1, n):
            prev = curr
            curr = curr.next
    
        # now 'curr' is node we want to remove
        # but if prev = None when n = 1, we need:
        if prev == None:
            head = curr.next
        else:
            prev.next = curr.next
        head = self.reverseList(head)
        return head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, present = None, head
        
        while(present):
            temp = present.next
            present.next = previous
            previous = present
            present = temp
        return previous


arr1 = [1, 2, 3, 4, 5, 6, 7]
list = ListNode(arr1[0])
list.addNode(arr1)

# Solve
a = Solution()
ans = a.removeNthFromEnd(list, 3)
res = []
while(ans):
    res.append(ans.val)
    ans = ans.next
print(res)