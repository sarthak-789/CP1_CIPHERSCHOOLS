# link : https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=helper=ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                helper.next=l1
                l1=l1.next
            else:
                helper.next=l2
                l2=l2.next
                
            helper=helper.next                
                
        if l1 is None:
            helper.next=l2
        else:
            helper.next=l1
        return res.next