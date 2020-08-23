# link : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        prev = None
        curr = head
        next = None
        
        while curr:
            next = curr.next
            if next and next.val == curr.val:
                while next and next.val==curr.val:
                    next = next.next
                
                if prev:
                    curr = next
                    prev.next = curr
                    
                else:
                    head = next
                    curr = head
            else:
                prev = curr
                curr = next
        
        return head