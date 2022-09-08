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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, present = None, head
        
        while(present):
            temp = present.next
            present.next = previous
            previous = present
            present = temp
        return previous

# Create the linked-list 'head' from arr = [1,2,3,4]
# 'head' will take the following form: 
# head = ListNode(arr[0], ListNode(arr[1], ListNode(arr[2], ListNode(arr[3]))))
arr = [1, 2, 9, 5, 2, 4]
head = ListNode(arr[0])
head.addNode(arr)

# Solve
a = Solution()
ans = a.reverseList(head)
res = []
while(ans):
    res.append(ans.val)
    ans = ans.next
print(res)