class Solution:
    def nearestPalindromic(self, n: str) -> str:
        int_n = int(n)
        if int_n < 11:
            return str(int_n - 1)

        if int_n == 11:
            return str(9)

        list_n = list(n)
        if n != n[::-1]:
            trans_p = list_n[:]
            trans_p_len = len(trans_p)
            for i in range(trans_p_len // 2):
                trans_p[trans_p_len - i - 1] = trans_p[i]
            # print(trans_p)
            int_trans_p = int("".join(trans_p))
            if int_trans_p > int_n:
                p_more = int_trans_p
                if int(trans_p[trans_p_len // 2]) > 0:
                    if trans_p_len % 2 == 0:
                        trans_p[trans_p_len // 2] = str(
                            int(trans_p[trans_p_len // 2]) - 1
                        )
                        trans_p[trans_p_len // 2 - 1] = str(
                            int(trans_p[trans_p_len // 2 - 1]) - 1
                        )
                    else:
                        trans_p[trans_p_len // 2] = str(
                            int(trans_p[trans_p_len // 2]) - 1
                        )

                else:
                    trans_p = list(
                        str(p_more - pow(10, trans_p_len - trans_p_len // 2 - 1))
                    )
                    trans_p_len = len(trans_p)
                    for i in range(trans_p_len // 2):
                        trans_p[trans_p_len - i - 1] = trans_p[i]

                p_less = int("".join(trans_p))

            if int_trans_p < int_n:
                p_less = int_trans_p
                if int(trans_p[trans_p_len // 2]) < 9:
                    if trans_p_len % 2 == 0:
                        trans_p[trans_p_len // 2] = str(
                            int(trans_p[trans_p_len // 2]) + 1
                        )
                        trans_p[trans_p_len // 2 - 1] = str(
                            int(trans_p[trans_p_len // 2 - 1]) + 1
                        )
                    else:
                        trans_p[trans_p_len // 2] = str(
                            int(trans_p[trans_p_len // 2]) + 1
                        )

                else:
                    trans_p = list(
                        str(p_less + pow(10, trans_p_len - trans_p_len // 2 - 1))
                    )
                    trans_p_len = len(trans_p)
                    for i in range(trans_p_len // 2):
                        trans_p[trans_p_len - i - 1] = trans_p[i]

                p_more = int("".join(trans_p))

        else:
            trans_p = list_n[:]
            trans_p_len = len(trans_p)
            int_trans_p = int("".join(trans_p))
            p_less = None
            p_more = None
            if int(trans_p[trans_p_len // 2]) == 0:
                trans_p = list(
                    str(int_trans_p - pow(10, trans_p_len - trans_p_len // 2 - 1))
                )
                trans_p_len = len(trans_p)
                for i in range(trans_p_len // 2):
                    trans_p[trans_p_len - i - 1] = trans_p[i]

                p_less = int("".join(trans_p))
            elif int(trans_p[trans_p_len // 2]) == 9:
                trans_p = list(
                    str(int_trans_p + pow(10, trans_p_len - trans_p_len // 2 - 1))
                )
                trans_p_len = len(trans_p)
                for i in range(trans_p_len // 2):
                    trans_p[trans_p_len - i - 1] = trans_p[i]

                p_more = int("".join(trans_p))

            trans_p = list_n[:]
            trans_p_len = len(trans_p)
            int_trans_p = int("".join(trans_p))
            if not p_more:
                if trans_p_len % 2 == 0:
                    trans_p[trans_p_len // 2] = str(int(trans_p[trans_p_len // 2]) + 1)
                    trans_p[trans_p_len // 2 - 1] = str(
                        int(trans_p[trans_p_len // 2 - 1]) + 1
                    )
                else:
                    trans_p[trans_p_len // 2] = str(int(trans_p[trans_p_len // 2]) + 1)
                p_more = int("".join(trans_p))

            trans_p = list_n[:]
            trans_p_len = len(trans_p)
            int_trans_p = int("".join(trans_p))
            if not p_less:
                if trans_p_len % 2 == 0:
                    trans_p[trans_p_len // 2] = str(int(trans_p[trans_p_len // 2]) - 1)
                    trans_p[trans_p_len // 2 - 1] = str(
                        int(trans_p[trans_p_len // 2 - 1]) - 1
                    )
                else:
                    trans_p[trans_p_len // 2] = str(int(trans_p[trans_p_len // 2]) - 1)
                p_less = int("".join(trans_p))
        # print(p_less, int_n, p_more)

        if int_n - p_less <= p_more - int_n:
            return str(p_less)
        else:
            return str(p_more)


s = Solution()
print(s.nearestPalindromic("10"))
print(s.nearestPalindromic("123456"))
print(s.nearestPalindromic("100"))
print(s.nearestPalindromic("11"))
print(s.nearestPalindromic("101"))
print(s.nearestPalindromic("111"))
print(s.nearestPalindromic("121"))
print(s.nearestPalindromic("191"))
