class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hashmap untuk menyimpan angka komplemen dari target
        komplemenMap = {}

        for i in range(len(nums)):
            if nums[i] in komplemenMap:
                return [komplemenMap[nums[i]], i]
            else:
                komplemenMap[target - nums[i]] = i

    def bruteForce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (target - nums[i] == nums[j]):
                    return [i, j]
