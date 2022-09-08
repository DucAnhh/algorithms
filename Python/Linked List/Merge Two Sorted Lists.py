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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr =  ans

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return ans.next

arr1 = [1, 2, 4]
list1 = ListNode(arr1[0])
list1.addNode(arr1)

arr2 = [1, 3, 4]
list2 = ListNode(arr2[0])
list2.addNode(arr2)

# Solve
a = Solution()
ans = a.mergeTwoLists(list1, list2)
res = []
while(ans):
    res.append(ans.val)
    ans = ans.next
print(res)