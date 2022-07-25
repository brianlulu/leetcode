# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        # input: l1 -> linked list; l2 -> linked list
        # output: sum of the linked list

        # constraints:
        # 0 <= node.val <= 9
        # guarrented that there is no leading 0 meaning the end of linked list
        # should not be 0

        # two pointer approach:
        # use two pointer for each head 
        # iterate through the both linked list and use a carry variable to keep track the carry on
        # when one of the linked list iterate to the end and the other have remaining
        # we should check with carry on first then we can just append to the result

        result = ListNode() # head = result.next
        curr = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            currSum = val1 + val2 + carry

            currNode = ListNode(val = currSum % 10) 
            carry = currSum // 10

            curr.next = currNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return result.next

        # TC: O(max(# of l1, # of l2))
        # SC: O(max(# of l1, # of l2)) if result is include