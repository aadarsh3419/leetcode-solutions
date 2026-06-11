# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        
        
        
        prev = None
        current = temp
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        new = head
        new1 = prev

        while new and new1:
            temp = new.next
            temp1 = new1.next
            new.next = new1
            
            new1.next = temp

            new = temp
            new1 = temp1
            