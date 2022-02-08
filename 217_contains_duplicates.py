from operator import contains


class Solution:
    def containsDuplicate(self, nums): 

        #input = [int]
        #output = bool
    
        hashmap = {}

        for item in nums:
            if item in hashmap:
                return True
            hashmap[item] = 1
        
        return False
    

if __name__ == "__main__":

    s = Solution()
    r1 = s.containsDuplicate([1,2,3,1])
    r2 = s.containsDuplicate([1,2,3,4])
    r3 = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

    print(r1, r2, r3)




        