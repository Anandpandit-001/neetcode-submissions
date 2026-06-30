class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return_list = []
        empty_dict = {}

        for val in nums:
            empty_dict[val] = empty_dict.get(val , 0) + 1
        
        # Sort keys by their frequency values in descending order and take the first k
        sorted_keys = sorted(empty_dict, key=empty_dict.get, reverse=True)
        return_list = sorted_keys[:k]

        return return_list