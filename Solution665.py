class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        counter = 0
        pre_max = nums[0]
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if counter != 0:
                    return False
                counter += 1
                if nums[i] < pre_max and i != 1:
                    nums[i] = nums[i-1]
            pre_max = nums[i-1]
        return True
