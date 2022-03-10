# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # input: head -> ListNode
        # output: reverse the linked list(head of reverse linked list) -> ListNode

#         # iterative 
#         cur = head
#         prev = None # newHead
        
#         while cur:
#             tmp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = tmp
        
#         return prev

        # recursive
        if not head:
            return None
        
        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)

            head.next.next = head
            
        head.next = None
            
        
        return new_head


'''
Time Complexity: O(N) for both approach because we are iterating through the whole linked list

Space Complexity: O(1) for iterative; O(N) for recursive because we are call N functions

'''