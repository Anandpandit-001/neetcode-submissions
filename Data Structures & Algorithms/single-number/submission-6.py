class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for val in nums:
            r ^= val
        return r
