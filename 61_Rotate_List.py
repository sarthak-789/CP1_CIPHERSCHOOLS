# link : https://leetcode.com/problems/rotate-list 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        shift=k%count
        if shift == 0:
            return head
        k=count-shift
        ptr=head
        for _ in range(k-1):
            ptr=ptr.next
        kth_node=ptr
        while ptr.next is not None:
            ptr=ptr.next
        ptr.next=head
        head=kth_node.next
        kth_node.next=None
        
        return head
        
        
        