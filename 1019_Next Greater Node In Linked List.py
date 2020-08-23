# link : https://leetcode.com/problems/next-greater-node-in-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        current = head
        res = []
        stack = []
        i = 0
        while current:
            res.append(0)
            value = current.val
            while stack and stack[-1][0] < value:
                _, index = stack.pop()
                res[index] = value
            
            stack.append((value, i))
            i += 1
            current = current.next
            
        return res