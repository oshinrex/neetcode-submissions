# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy

        node1 = l1
        node2 = l2

        while node1 or node2:
            if node1 and node2:
                curr.next = ListNode((node1.val + node2.val + carry)%10, None)
                carry = (node1.val + node2.val + carry) // 10

                node1 = node1.next
                node2 = node2.next
            elif node1:
                curr.next = ListNode((node1.val + carry)%10, None)
                carry = (node1.val + carry) // 10
                node1 = node1.next
            else:
                curr.next = ListNode((node2.val + carry)%10, None)
                carry = (node2.val + carry) // 10
                node2 = node2.next
            
            curr = curr.next 
        
        if carry != 0:
            curr.next = ListNode(carry, None)
        
        return dummy.next
