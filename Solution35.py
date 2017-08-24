class Solution(object):
    def search(self, nums, l, r, target):
        if r < l:
            return l
        mid = (l + r) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums, l, mid-1, target)
        else:
            return self.search(nums, mid+1, r, target)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search(nums, 0, len(nums)-1, target)
