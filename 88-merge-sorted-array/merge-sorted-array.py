class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2 and a pointer for the merged array
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # While there are elements in both arrays
        while p1 >= 0 and p2 >= 0:
            # Compare the elements from the end of both arrays
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]