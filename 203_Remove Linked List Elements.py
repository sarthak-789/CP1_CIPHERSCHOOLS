#link : https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        ptr=head
        while ptr is not None and ptr.val==val:
            ptr=ptr.next
        head=ptr
        if head == None:
            return head
        ptr=head
        while ptr.next is not None:
            if ptr.next.val==val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head
        