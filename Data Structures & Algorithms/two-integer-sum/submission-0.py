class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}  # Stores {number: index}
        
        for i, val in enumerate(nums):
            complement = target - val
            
            # If the complement exists in our dictionary, we found our pair!
            if complement in seen_dict:
                return [seen_dict[complement], i]
            
            # Otherwise, add the current number and index to the dictionary
            seen_dict[val] = i
