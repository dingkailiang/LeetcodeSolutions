METHOD = "twoSum"

TESTCASES = [
    ([2,7,11,15],9),
    ([-1,-2,-3,-4,-5],-8)
]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]