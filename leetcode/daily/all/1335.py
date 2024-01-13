from itertools import combinations


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        if d == 1:
            return max(jobDifficulty)

        len_diff = len(jobDifficulty)
        if d > len_diff:
            return -1
        elif d == len_diff:
            return sum(jobDifficulty)
        else:
            sep_index = combinations(range(1, len_diff), d - 1)
            difficulty = []
            for case in sep_index:
                # print(case)
                buckets = []
                buckets.append(jobDifficulty[0 : case[0]])
                for i in range(len(case) - 1):
                    buckets.append(jobDifficulty[case[i] : case[i + 1]])
                buckets.append(jobDifficulty[case[-1] :])
                # print(buckets)
                difficulty.append(sum([max(bucket) for bucket in buckets]))
            # print(difficulty)
            return min(difficulty)


s = Solution()
print(s.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
print(s.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=1))
