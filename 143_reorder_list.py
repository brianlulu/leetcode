# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # input: head -> ListNode
        # ouput: None modify the linked list as the question asked
        
        # constraints:
        # # of nodes >= 1

        # two pointer + fast slow pointer approach:
        # from the question we know that the reorder will link head and tail
        # of the linked list 
        # L_0 -> L_n -> L_1 -> L_n-1 -> L_2 -> L_n-2 ...
        # Therefore, we can use two pointer "curr" and "tail" to iterate through
        # the linked list and modify the list. However, this is a singly linked-list
        # the tail pointer can not traverse to previous node. To solve this, we can
        # reverse the order at the second part of the linked list. However, we need
        # to know which is the starting node for second part of linked list. We can use
        # fast slow pointer. In this method, the fast pointer start at second node and 
        # slow start at first node. Then, fast traverse two and slow traverse one

        # find mid pointer
        slow = head
        fast = head.next

        # one element or two element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        
        # reverse second part
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        
        # new head of second list, when reverse the second will iterate to the null
        second = prev 
        
        # reorder
        while second:
            tmpFirst, tmpSecond = first.next, second.next
            first.next = second
            second.next = tmpFirst
            first = tmpFirst
            second = tmpSecond
        
        # TC: O(N) iterate through every element in list
        # SC: O(1)