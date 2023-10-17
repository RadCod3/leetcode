class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if (
                    (stack[-1] == "(" and char == ")")
                    or (stack[-1] == "[" and char == "]")
                    or (stack[-1] == "{" and char == "}")
                ):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
