# link : https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        st=ptr=head
        qtr=head.next
        while ptr and qtr:
            while ptr.val==qtr.val:
                ptr=ptr.next
                qtr=qtr.next
                if ptr==None or qtr==None:
                    break

            st.next=qtr
            if ptr==None or qtr==None:
                break
            ptr=ptr.next
            qtr=qtr.next
            st=st.next
        return head
            
        