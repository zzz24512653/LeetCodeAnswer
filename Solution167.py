class Solution(object):
    def search(self, numbers, i, j, target):
        if j < i:
            return -1
        mid = int((i + j) / 2)
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return self.search(numbers, i, mid-1, target)
        else:
            return self.search(numbers, mid+1, j, target)

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n):
            j = self.search(numbers, i+1, n-1, target-numbers[i])
            if j != -1:
                return [i+1, j+1]
