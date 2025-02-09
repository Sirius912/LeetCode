class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged_array = nums1 + nums2
        merged_array.sort()
        length = len(merged_array)
        
        if length % 2 == 1:
            index = length // 2
            return merged_array[index]
        else:
            index1 = length // 2 - 1
            index2 = index1 + 1
            median = (merged_array[index1] + merged_array[index2]) / 2.0
            return median