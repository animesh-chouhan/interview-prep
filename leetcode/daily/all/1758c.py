def gen_next():
    while True:
        yield "0"
        yield "1"


class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        for i, d in zip(gen_next(), s):
            if i != d:
                count1 += 1
            if i == d:
                count2 += 1

        return min(count1, count2)
