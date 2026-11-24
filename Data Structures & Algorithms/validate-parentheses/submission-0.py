class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if stack and s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif stack and s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack) == 0 
        