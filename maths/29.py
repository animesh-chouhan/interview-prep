class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mult = 1
        if dividend < 0:
            dividend = -dividend
            mult = -mult
        if divisor < 0:
            divisor = -divisor
            mult = -mult

        quotient = 0
        while dividend - divisor > 0:
            dividend -= divisor
            quotient += 1

        return quotient * mult


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mult = 1
        if dividend < 0:
            dividend = -dividend
            mult = -mult
        if divisor < 0:
            divisor = -divisor
            mult = -mult

        quotient = 0
        div_list = [divisor]
        quo_list = [1]
        while True:
            # print(div_list)
            # print(quo_list)
            # print(dividend, div_list[-1])
            # print(quotient)
            if dividend - div_list[-1] < 0:
                while dividend - divisor >= 0:
                    # print(dividend, quotient)
                    for i, div in enumerate(div_list):
                        if dividend - div < 0:
                            # print(i)
                            if i - 1 >= 0:
                                dividend -= div_list[i - 1]
                                quotient += quo_list[i - 1]
                            break
                val = quotient * mult
                v2_31 = pow(2, 31)
                # if val > v2_31 - 1:
                #     return v2_31 - 1
                # elif val < -v2_31:
                #     return -v2_31
                # else:
                return val

            dividend -= div_list[-1]
            quotient += quo_list[-1]
            div_list.append(div_list[-1] + div_list[-1])
            quo_list.append(quo_list[-1] + quo_list[-1])


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mult = 1
        if dividend < 0:
            dividend = -dividend
            mult = -mult
        if divisor < 0:
            divisor = -divisor
            mult = -mult

        quotient = 0
        div_list = [divisor]
        quo_list = [1]
        while True:
            if dividend - div_list[-1] < 0:
                while dividend - divisor >= 0:
                    for i, div in enumerate(div_list):
                        if dividend - div < 0:
                            if i - 1 >= 0:
                                dividend -= div_list[i - 1]
                                quotient += quo_list[i - 1]
                            break
                val = quotient * mult
                return min(max(-2147483648, val), 2147483647)

            dividend -= div_list[-1]
            quotient += quo_list[-1]
            div_list.append(div_list[-1] + div_list[-1])
            quo_list.append(quo_list[-1] + quo_list[-1])


s = Solution()
print(s.divide(pow(2, 31), 1))
# print(s.divide(2147483646, 1))
