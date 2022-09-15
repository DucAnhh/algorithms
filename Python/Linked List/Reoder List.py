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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # count the number of nodes in the linked-list
        count = 0
        node = head
        while node != None:
            count = count + 1
            node = node.next
            
        # find mid and split
        node = head
        mid = int(np.ceil(count/2))
        for i in range(mid):
            if i == mid - 1:
                head1 = node.next
                node.next = None
            else:
                node = node.next
        
        # Now we have two linked-lists 'head' and 'head1'
        head1 = self.reverseList(head1)
        head = self.mergeTwoLists(head, head1)
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, present = None, head
        
        while(present):
            temp = present.next
            present.next = previous
            previous = present
            present = temp
        return previous 
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr =  ans

        while list1 and list2:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return ans.next


arr1 = [1, 2, 3, 4, 5, 6, 7]
list = ListNode(arr1[0])
list.addNode(arr1)

# Solve
a = Solution()
ans = a.reorderList(list)
res = []
while(ans):
    res.append(ans.val)
    ans = ans.next
print(res)