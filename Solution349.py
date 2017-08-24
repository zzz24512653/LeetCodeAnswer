class Solution(object):
    def binary_search(self, nums, i, j, target):
        if j < i:
            return -1
        mid = int((i+j) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, i, mid-1, target)
        else:
            return self.binary_search(nums, mid+1, j, target)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = sorted(list(set(nums1)))
        ret = []
        for n in set(nums2):
            print(n, nums)
            if self.binary_search(nums, 0, len(nums)-1, n) != -1:
                ret.append(n)
        return ret
