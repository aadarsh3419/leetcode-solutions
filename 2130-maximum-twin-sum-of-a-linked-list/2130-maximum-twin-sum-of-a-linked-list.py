# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        link = head
        maps = {}
        n = 0
        while link:
            maps[n] = link.val 
            link = link.next
            n+=1
        maxx = 0
        for i in range(n//2):
           k = n-1-i
           maxx = max(maxx,maps[i]+maps[k])
        return maxx 
 