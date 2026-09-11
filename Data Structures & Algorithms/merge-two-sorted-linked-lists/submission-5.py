# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dummy = ListNode(0)
        curr = dummy 

        while p1 or p2:
            if not p1:
                curr.next = p2
                break

            if not p2:
                curr.next = p1
                break
            
            if p1.val <= p2.val: 
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            
            curr = curr.next
        
        return dummy.next
