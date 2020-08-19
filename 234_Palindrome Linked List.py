# link: https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        helper=ListNode()
        helper.next=head
        l=[]
        flag=Truea
        while helper is not None:
            l.append(helper.val)
            helper=helper.next
        while head is not None:
            i=l.pop()
            if head.val==i:
                flag=True
            else:
                flag=False
                break
            head=head.next
        return flag