from itertools import combinations


def all_subsequences(nums):
    all = []
    for l in range(1, len(nums) + 1):
        all.append(list(combinations(nums, l)))
    print(all)
    return all


all_subsequences([10, 9, 2, 5, 3, 7, 101, 18, 11, 13])
