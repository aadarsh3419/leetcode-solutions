# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        hashs = {}
        n = 0
        mid = head
        while mid:
            hashs[n] = mid
            mid = mid.next
            n+=1
        mid = n//2
        prev = hashs[mid-1]
        prev.next = hashs[mid].next
        return head