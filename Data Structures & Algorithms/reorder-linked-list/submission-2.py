# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint 
        slow = head
        fast = head
        prev = None

        while fast and fast.next: 
            prev = slow # 2, 4
            slow = slow.next # 4, 6
            fast = fast.next.next # 6, None

        # odd vs even
        p2 = None 
        if fast: 
            p2 = slow.next
            slow.next = None
        else:
            p2 = slow # p2 = 6
            prev.next = None  
        
        p1 = head

        # reverse second half of list 
        prev, curr = None, p2
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 
        
        dummy = ListNode(0)
        p2 = prev 
        p = dummy
        # interweave two lists created 
        while p1 or p2:
            p.next = p1
            p1 = p1.next
            p = p.next

            if p2:
                p.next = p2
                p2 = p2.next
                p = p.next

        head = dummy.next