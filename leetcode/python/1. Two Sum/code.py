class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in nums:
            nums2 = nums.copy()
            nums2.remove(number)
            num = target - number
            if num in nums2:
                return [nums.index(number), nums2.index(num) + 1]
