# link : https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ptr=qtr=head
        while ptr and qtr and qtr.next:
            ptr=ptr.next
            qtr=qtr.next.next
            
            if ptr==qtr:
                ptr=head
                while ptr:
                    if ptr==qtr:
                        return ptr
                    else:
                        ptr=ptr.next
                        qtr=qtr.next
        return None
                    
        