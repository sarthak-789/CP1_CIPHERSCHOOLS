# link : https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ptr=head
        res=qtr=head.next
        while ptr and qtr:
            temp1 = qtr.next
            qtr.next = ptr
            if temp1 == None:
                ptr.next = None
                break
            if temp1.next == None:
                ptr.next = temp1
                break
            ptr.next = temp1.next
            ptr = temp1
            qtr = temp1.next
        return res