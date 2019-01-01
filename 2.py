# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_numbers(ll):
            num = ""
            while(ll is not None):
                num = num + str(ll.val)
                ll = ll.next
            return str(num)
        def rev_num(num):
            return int(str(num)[::-1])
        to_ret_num = rev_num(get_numbers(l1)) + rev_num(get_numbers(l2))
        print(to_ret_num)
        if to_ret_num == 0:
            return ListNode(0)
        dummy = ListNode(0)
        to_ret = dummy
        while(to_ret_num > 0):
            dummy.next = ListNode(to_ret_num%10)
            to_ret_num//=10
            dummy = dummy.next
        return to_ret.next
