# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        # input: list1 -> ListNode, list2 -> ListNode
        # output sorted merged list -> ListNode
        
        dummy_head = ListNode()
        tails = dummy_head
        
        # iterate through each list one by one and compare
        while list1 and list2:
            # if equal use list1
            if list1.val < list2.val:
                tails.next = list1
                list1 = list1.next
            else:
                tails.next = list2
                list2 = list2.next
            tails = tails.next
        
        if list1:
            tails.next = list1
        
        if list2:
            tails.next = list2
           

        return dummy_head.next

'''
Time Complexity: O(N + M)  M = list1.length and N = list2.length 

Space Complexity: O(1)
'''
            
        