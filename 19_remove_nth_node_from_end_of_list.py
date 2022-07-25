# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):

        
        # input: head -> ListNode; n -> int
        # output: head of the modify linked list -> ListNode

        # constraints:
        # sz = size of the linked list
        # sz >= n >= 1

        # two pointer approach:
        # we can use a left right pointer such that left always are n + 1 away from right pointer
        # in this way, when the right pointer reach to the end of the linked list.
        # the left pointer will be on n+1th node from the end and we can just directly connect
        # n + 1 node and n - 1 node together. Also, to avoid edge case such that the left pointer does
        # not have n + 1 node from the back. We use a dummy node at the beginning that connect to head


        dummy = ListNode(next = head)
        l = dummy

        for i in range(n):
            head = head.next
            r = head
        
        while r:
            l = l.next
            r = r.next

        nthNode = l.next
        l.next = nthNode.next

        return dummy.next


        # TC: O(N)
        # SC: O(1)
    
