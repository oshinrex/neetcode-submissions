# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        curr = head

        while curr:
            # find section to reverse
            h = curr 
            count = k

            p = None
            while curr and count > 0:
                p = curr
                curr = curr.next
                
                count -= 1
            
            if count != 0:
                prev.next = h
            else:
                # reverse
                p.next = None 

                curr_last = h
                curr_p = None
                while h:
                    temp = h.next
                    h.next = curr_p
                    curr_p = h
                    h = temp
                
                prev.next = curr_p
                prev = curr_last
            
        return dummy.next