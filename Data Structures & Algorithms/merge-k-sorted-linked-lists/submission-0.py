# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in range(len(lists)//2): 
            l1 = lists[2*i]
            l2 = lists[2*i+1]
            lst.append(self.merge(l1, l2))
        
        if len(lists) % 2: 
            lst.append(lists[-1])
        
        if len(lst) == 1: 
            return lst[0]
        elif len(lst) == 0:
            return None
        else: 
            return self.mergeKLists(lst)
    
    def merge(self, l1, l2): 
        dummy = ListNode(0, None)
        curr = dummy
        h1 = l1
        h2 = l2

        while h1 or h2: 
            if not h1: 
                curr.next = h2
                h2 = None
            elif not h2: 
                curr.next = h1
                h1 = None 
            else: 
                if h1.val <= h2.val: 
                    curr.next = h1
                    curr = curr.next
                    h1 = h1.next 
                else: 
                    curr.next = h2
                    curr = curr.next 
                    h2 = h2.next 
        
        return dummy.next
