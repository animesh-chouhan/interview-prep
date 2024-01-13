class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = 0
        c = 0
        for i, char in enumerate(s):
            if char == "(":
                o += 1
            else:
                if o:
                    o -= 1
                else:
                    c += 1

        # print(o, c)
        return o + c


s = Solution()
print(s.minAddToMakeValid("())"))
print(s.minAddToMakeValid(")())"))
print(s.minAddToMakeValid("((("))
print(s.minAddToMakeValid("((((((((((((((((((((((((()))))))))))())))))))))))))))"))
