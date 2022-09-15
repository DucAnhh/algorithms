# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This code only run successfully in web Leetcode 
# because I haven't create linked-list with cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # complexity O(n)
        node =  head
        hashset = []
        while node != None:
            if node not in hashset:
                hashset.append(node)
                node = node.next
            else:
                return True
        return False
        
        # complexity O(1)
#         slow, fast = head, head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False