class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        result = 0
        for i in range(length):
            if nums[i] >= target:
                result = i
                break
            else:
                result = i + 1
        return result