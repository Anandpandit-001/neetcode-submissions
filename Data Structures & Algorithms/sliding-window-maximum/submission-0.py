class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        fixed_size_array = [0] * k
        return_array = []

        # FIX 1: Use 'k' instead of hardcoding 3
        for i in range(k):
            fixed_size_array[i] = nums[i]

        first_max = max(fixed_size_array)
        return_array.append(first_max)
        
        # FIX 2: j should start at the next element to process, which is index k
        j = k 
        
        # FIX 3: strictly less than len(nums) to avoid out of bounds
        while j < len(nums):
            for i in range(k - 1):
                fixed_size_array[i] = fixed_size_array[i + 1]
            
            # FIX 4: Add the actual number from the array, not the index 'j'
            fixed_size_array[k - 1] = nums[j]
            return_array.append(max(fixed_size_array))
            j += 1

        return return_array