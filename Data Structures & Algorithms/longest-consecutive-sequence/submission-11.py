from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sorted_list = sorted(nums)
        # Start counting at 1, because a single number is a sequence of 1
        current_lon = 1
        longest_seq = 1
        
        for i in range(len(sorted_list) - 1):
            # 1. Ignore duplicates completely
            if sorted_list[i] == sorted_list[i+1]:
                continue 
                
            # 2. If consecutive, increment the count
            elif sorted_list[i] + 1 == sorted_list[i+1]:
                longest_seq += 1
                current_lon = max(current_lon, longest_seq)
                
            # 3. If the chain breaks, reset the count back to 1
            else:
                longest_seq = 1
                
        return current_lon