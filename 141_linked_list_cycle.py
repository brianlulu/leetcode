# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        
        # input: head -> ListNode
        # output: whether a cyclic linked list -> Boolean


#         hash_set = set()
#         cur = head
        
#         while cur:
            
#             if cur in hash_set:
#                 return True
#             else:
#                 hash_set.add(cur)
            
#             cur = cur.next
            
        
#         return False
        
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
            
        return False
    

'''
Time Complexity: O(N) because the worst case of slow faster pointer is that 
    the distance between slow fast pointer is N-1, meaning that the cyclic point at index 0
    O(N) for hashset because we iterate through the whole linked list
Space Complexity: O(1) for slow fast pointer
    O(N) for hashset
'''