class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        self.nums = nums
        self.target = target
        for n, first in enumerate(nums, start=0):
            for m, second in enumerate(nums[n+1:], start=n+1):
                if (first + second) == target:
                    first_index = n
                    second_index = m
        return [first_index, second_index]

example_1 = Solution()
print(f"Example 1, nums = [2,7,11,15], target = 9: {example_1.twoSum(nums = [2,7,11,15], target = 9)}")

example_2 = Solution()
print(f"Example 2, nums = [3,2,4], target = 6: {example_2.twoSum(nums = [3,2,4], target = 6)}")

example_3 = Solution()
print(f"Example 3, nums = [3,3], target = 6: {example_3.twoSum(nums = [3,3], target = 6)}")