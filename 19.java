/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode new_head = new ListNode(1);
        ListNode temp = new_head;
        int count = 0;
        Queue<Integer> q = new LinkedList<>(); 
        while(head != null){
            q.add(head.val);
            head = head.next;
        }
        int length = q.size();
        int from_back = length - n;
        boolean removed = false; 
        while(q.size() != 0){
            int add = q.remove();
            if(from_back == 0 && !removed){
                removed = true;
                continue;
            }
            new_head.next = new ListNode(add);
            new_head = new_head.next;
            from_back-=1;
        }
        return temp.next;
    }
}