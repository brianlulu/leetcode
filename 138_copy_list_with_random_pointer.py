
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
         
        # intput: head ->　Node
        # output: new head -> Node

        # constraints:
        # n is linked list size
        # n >= 0
        # random is only pointing to null or node in the linked list

        # hashmap approach:
        # iterate through the linked list twice
        # use hashmap to map the old node to the copy node {oldNode : copyNode}
        # to avoid the uncreated copy node
        # first iteration: simply copy the node with value but leave next and random null
        # map with the old with new copy
        # second iteration: iterate through the linked list again, so that we can update the copy's next and random
        # with the help of the hashmap

        hashMap = {None:None}

        # create the first copy
        curr = head
        while curr:
            copy = Node(x = curr.val)
            hashMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hashMap[curr]
            copy.next = hashMap[curr.next]
            copy.random = hashMap[curr.random]
            curr = curr.next


        return hashMap[head] 

        # TC: O(N) iterate through the list twice but in two different loop
        # SC: O(N)