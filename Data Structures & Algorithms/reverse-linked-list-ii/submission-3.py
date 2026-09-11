# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = None
        curr = dummy
        count = 0


        while count != left: 
            prev = curr
            curr = curr.next 
            count += 1
        
        p1 = curr
        p2 = None

        end = p1

        while count != right + 1: 
            temp = p1.next 
            p1.next = p2
            p2 = p1
            p1 = temp 
            count += 1
        
        prev.next = p2
        end.next = p1

        return dummy.next

