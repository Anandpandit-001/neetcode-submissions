class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        # Simply XOR every single number into the running total
        for val in nums:
            result ^= val
            
        return result
