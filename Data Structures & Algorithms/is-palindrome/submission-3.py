class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        l = len(s) - 1

        while i < l:
            # Skip non-alphanumeric characters from the left
            while i < l and not s[i].isalnum():
                i += 1
                
            # Skip non-alphanumeric characters from the right
            while i < l and not s[l].isalnum():
                l -= 1
                
            # Compare the characters in lowercase
            if s[i].lower() != s[l].lower():
                return False
            
            # MOVE THE POINTERERS to avoid the infinite loop!
            i += 1
            l -= 1

        return True