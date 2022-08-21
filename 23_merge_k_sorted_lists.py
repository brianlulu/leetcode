# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        
        # input: lists -> List[ListNode]
        # output: merged linked list -> ListNode

        # constraints:
        # 0 <= lists
        
        # merge two lists approach:
        # use the merge two sorted lists functions and then just merge two of them
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            result = []

            for i in range(0, len(lists), 2):
                listA = lists[i]
                listB = lists[i+1] if (i+1) < len(lists) else None

                result.append(self.mergeLists(listA, listB))
            
            lists = result
        
        return result[0]

    def mergeLists(self, listA, listB):
        # return the merged sorted list from listA and listB

        result = ListNode()

        curA, curB, curResult = listA, listB, result

        while curA and curB:
            if curA.val > curB.val:
                curResult.next = curB
                curB = curB.next
            else:
                curResult.next = curA
                curA = curA.next
            
            curResult = curResult.next

        if curA:
            curResult.next = curA    

        if curB:
            curResult.next = curB

        return result.next

if __name__ == "__main__":

    s1 = Solution()

    print(s1.mergeLists([], None))