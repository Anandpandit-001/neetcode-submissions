class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack  = []
        mapping = { ")" : "(" , "]" : "[", "}" : "{" }

        for char in s:
            if char in mapping:

                if len(stack) == 0 or stack[-1] != mapping[char]:
                    return False

                if stack[-1] == mapping[char]:
                    stack.pop()

            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False