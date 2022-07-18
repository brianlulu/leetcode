class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        
        # input: target -> int, position -> List[int], speed -> List[int]
        # output: number of car fleets that will arrive at desitination

        # constraints:
        # target > 0 and target > position[i]
        # position.length > 0 speed.length > 0
        # all the values in position are unique 
        # speed > 0

        # stack approach:
        # first create a new array with tuple of (position, speed) called "car"
        # and sorted the array by the position with increasing order
        # we iterate through the car array in reversed order
        # because if we iterate in the original order we cannot make sure which 
        # car collade first, meaning the middle car might collade with the car 
        # in front of it before the first car collade with the middle car
        # to solve that, we iterate through backward because if the last car
        # is slower than the second last car, it will collade with the last car
        # and for sure travel at the speed of last car 
        # we use stack to keep track the car because the last car fleet (the one closed to target) should be 
        # deal with last

        pair = [(p, s) for p, s in zip(position, speed)]
        
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)    

        # TC: O(NlogN) for sorting: O(N) for iterate through car
        # SC: O(N): all cars dont collade