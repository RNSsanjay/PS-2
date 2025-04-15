class Solution:
    def minimumRemovals(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = bisect_left(sorted_nums, nums[i])
        return len(nums) - max(dp)
