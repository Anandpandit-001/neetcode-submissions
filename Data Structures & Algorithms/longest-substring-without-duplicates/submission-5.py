class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        i = 0
        max_val = 0
        return_val = 0
        if len(s) == 0:
            return 0
        if not s.strip():
            return 1
        if len(s) == 1:
            return 1
        
        for character in s:
            if character in dictionary:
                #max_val = max_val - dictionary[character] 
                if max_val > return_val:
                    return_val = max_val

                max_val = i - dictionary[character]
                dictionary = {key: value for key, value in dictionary.items() if value > dictionary[character]}
                dictionary[character] = i
                
                
            else:
                dictionary[character] = i
                max_val = max_val + 1
            
            i = i + 1

        return max(return_val, max_val)
