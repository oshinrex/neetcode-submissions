# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint 
        midpoint = head
        f = head 

        while f and f.next:
            midpoint = midpoint.next
            f = f.next.next

        # reverse from midpoint 
        prev = None 
        curr = midpoint.next
        midpoint.next = None

        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp 

        start = head 
        end = prev 

        # merge head and end 
        while end: 
            temps = start.next
            tempe = end.next

            start.next = end
            end.next = temps

            start = temps
            end = tempe
        
        




