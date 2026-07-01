class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_dict = defaultdict(list)
        for val in strs:
            sorted_val = tuple(sorted(val))
            empty_dict[sorted_val].append(val)

        values_list = list(empty_dict.values())

        return values_list
