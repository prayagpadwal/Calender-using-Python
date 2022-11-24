# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = head

        while h1:
            while h1.next and h1.next.val == h1.val:
                h1.next = h1.next.next
            h1 = h1.next
        return head