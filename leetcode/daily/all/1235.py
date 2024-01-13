from functools import cache
from bisect import bisect, bisect_left


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        max_profit = [0] * len(startTime)

        combined = sorted(
            list(zip(startTime, endTime, profit)), key=lambda item: item[1]
        )
        # print(combined)

        for i in range(len(startTime)):
            max_profit[i] = max(
                [
                    combined[i][2] + max_profit[k]
                    for k in range(i)
                    if combined[k][1] <= combined[i][0]
                ],
                default=combined[i][2],
            )

        # print(max(max_profit))
        return max(max_profit)


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        @cache
        def max_profit(i):
            return max(
                [
                    profit[i] + max_profit(k)
                    for k in range(len(startTime))
                    if endTime[k] <= startTime[i]
                ],
                default=profit[i],
            )

        return max([max_profit(i) for i in range(len(startTime))])


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        max_profit = [0] * len(startTime)

        combined = sorted(
            list(zip(startTime, endTime, profit)), key=lambda item: item[1]
        )
        # print(combined)

        for i in range(len(startTime)):
            max_profit[i] = max(
                [
                    combined[i][2] + max_profit[k]
                    for k in range(
                        bisect(combined, combined[i][0], 0, i, key=lambda item: item[1])
                    )
                ],
                default=combined[i][2],
            )

        print(max_profit)
        return max(max_profit)


# Take or not take memoization
class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        combined = sorted(list(zip(startTime, endTime, profit)))
        # print(combined)

        @cache
        def max_profit(i):
            if i >= len(combined):
                return 0
            # not take current
            ret = max_profit(i + 1)

            # take current
            next_i = bisect_left(
                combined, combined[i][1], i, len(combined), key=lambda item: item[0]
            )
            ret = max(ret, combined[i][2] + max_profit(next_i))
            return ret

        return max_profit(0)


# Take or not take iterative
class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        combined = sorted(
            list(zip(startTime, endTime, profit)), key=lambda item: item[1]
        )
        # print(combined)

        max_profit = [0] * len(startTime)
        max_profit[0] = combined[0][2]

        for i in range(1, len(combined)):
            start, end, profit = combined[i]
            # Take current
            last_i = bisect(combined, start, 0, i, key=lambda item: item[1]) - 1
            max_profit[i] = max(
                profit + (max_profit[last_i] if last_i >= 0 else 0), max_profit[i - 1]
            )

        # print(max_profit)
        return max(max_profit)


s = Solution()
print(
    s.jobScheduling(
        startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
    )
)
print(
    s.jobScheduling(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
)
print(s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
# print(s.jobScheduling())
