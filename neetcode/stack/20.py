from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if len(stack) > 0:
                    popped = stack.pop()
                    match c:
                        case ")":
                            if popped != "(":
                                return False
                        case "]":
                            if popped != "[":
                                return False
                        case "}":
                            if popped != "{":
                                return False
                else:
                    return False
        return True if len(stack) == 0 else False
