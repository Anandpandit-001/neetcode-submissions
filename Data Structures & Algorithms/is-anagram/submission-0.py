class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        empty_dictionary = {}
        for c in s:
            empty_dictionary[c] = empty_dictionary.get(c,0) + 1

        for c in t:
            empty_dictionary[c] = empty_dictionary.get(c , 0) - 1

        return all(v == 0 for v in empty_dictionary.values())