# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self,head,k):
        if k==1:
            return head
        cur=self.reverse(head.next,k-1)
        head.next.next=head
        head.next=None
        return cur
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p=head
        i=0
        while p and i<k:
            p=p.next
            i+=1
        if i<k:
            return head
        newhead=self.reverse(head,k)
        head.next=self.reverseKGroup(p,k)
        return newhead
        