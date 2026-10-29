class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        m -= 1
        n -= 1 
        # get the actual endings of arrays
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n]
                last -= 1
                n -= 1

        # if n is greater than m, fill the nums1 with leftover nums2 elements 
        while n >= 0:
            nums1[last] = nums2[n]
            n, last = n - 1, last - 1