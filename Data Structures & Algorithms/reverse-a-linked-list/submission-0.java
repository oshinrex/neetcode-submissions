/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode start = head; 
        ListNode temp = null; 

        while (start != null) {
            temp = start.next;
            start.next = prev;
            prev = start;
            start = temp;
        }

        return prev;
    }
}
