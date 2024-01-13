class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = []
        c = []
        for i, char in enumerate(s):
            if char == "(":
                o.append(i)
            else:
                if o:
                    o.pop()
                else:
                    c.append(i)

        # print(o, c)
        return len(o) + len(c)


s = Solution()
print(s.minAddToMakeValid("())"))
print(s.minAddToMakeValid(")())"))
print(s.minAddToMakeValid("((("))
print(s.minAddToMakeValid("((((((((((((((((((((((((()))))))))))())))))))))))))))"))
