class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        # input: nums1 -> List[int], nums2 -> List[int]
        # output: median of of the merged of the two sorted array -> float

        # constraints:
        # num1.length nums2.length >= 0
        # num1.length + nums2.length >= 1
        
        # binary search approach:
        # To find the median, we bascially just find the middle element(s) in the merged of the two sorted array
        # In this sense, we are bascially partioning the merged array into left and righ in the middle
        # However, it is not efficient to merge the two array. Therefore, we should apply binary search to
        # find the left part of the merged array because we do not need to know everything from the right part


        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 # floor division handles the odd and even

        # find the shorter array and we perform binary search on that
        if len(A) > len(B):
            A, B = nums2, nums1 
        l, r = 0, len(A) - 1
        
        while l <= r:
            midA = (l + r) // 2
            remainB = half - midA - 2 # (half - 1) - (midA - 1)
            
            ALeft = A[midA] if midA >= 0 else float("-infinity")
            ARight = A[midA+1] if midA + 1 < len(A) else float("infinity")
            BLeft = B[remainB] if remainB >= 0 else float("-infinity")
            BRight = B[remainB+1] if remainB + 1 < len(B) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight:
                # odd 
                if total % 2:
                    return min(ARight, BRight)
                # even
                return (max(ALeft,BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = midA - 1
            else:
                l = midA + 1 
        
        #TC: O(log(min(n, m)) we only apply binary search on the shorter array
        #SC: O(1)
        