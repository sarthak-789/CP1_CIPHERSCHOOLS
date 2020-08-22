# link : https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=dummy=ListNode(0)
        b=0
        while l1 or l2 or b:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sm= v1 + v2 + b
            a=sm%10
            b=sm//10
            helper=ListNode(a)
            dummy.next=helper
            dummy=dummy.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return res.next