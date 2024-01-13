class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)

        if len(str_num) == 1:
            return 8

        if str_num[0] == "9":
            for digit in str_num:
                if digit != "9":
                    a = str_num.replace(digit, "9")
                    break
            else:
                a = str_num
        else:
            a = str_num.replace(str_num[0], "9")

        if str_num[0] == "1":
            for digit in str_num:
                if digit != "1" and digit != "0":
                    b = str_num.replace(digit, "0")
                    break
            else:
                b = str_num
        else:
            b = str_num.replace(str_num[0], "1")

        return int(a) - int(b)
