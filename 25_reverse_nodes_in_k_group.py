# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):

        result = ListNode(0, head)
        groupPrev = result

        while True:
            kthNode = self.getKthNode(groupPrev,k)
            if not kthNode:
                break
        
            groupNext = kthNode.next
        
            # reverse group
            prev, curr = groupNext, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp

        return result.next


    def getKthNode(self, curr, k):
        # get the kth node from curr node

        while k > 0 and curr:
            curr = curr.next
            k -= 1
        
        return curr

# TC: O(N)
# SC: O(1)
