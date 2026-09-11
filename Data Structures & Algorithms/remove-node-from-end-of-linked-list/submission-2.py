# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr:
            curr = curr.next
            count += 1
        
        steps = count - n - 1
        print(steps)
        curr = dummy 
        print(curr.val)
        prev = None

        while steps > 0: 
            prev = curr
            curr = curr.next
            steps -= 1
        
        curr.next = curr.next.next
        return dummy.next