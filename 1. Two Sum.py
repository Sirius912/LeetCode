class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                else:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]
