class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ret = ["" for _ in range(numRows)]
        i = 0
        mult = 1
        for char in s:
            # print(i)
            ret[i] += char
            i += 1 * mult
            if i <= 0 or i >= numRows - 1:
                mult *= -1

        return "".join(ret)


s = Solution()
print(s.convert("PAYPALISHIRING", 1))
