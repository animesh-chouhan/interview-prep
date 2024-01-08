# Divide nums in k parts in order such that each part has atleast one element
from functools import lru_cache
from itertools import combinations


# Brute force + combinatorics
def divide(nums, k):
    sep_indexes = combinations(range(1, len(nums)), k - 1)
    buckets = []
    for case in sep_indexes:
        # print(case)
        bucket = []
        bucket.append(nums[0 : case[0]])
        for i in range(len(case) - 1):
            bucket.append(nums[case[i] : case[i + 1]])
        bucket.append(nums[case[-1] :])
        buckets.append(bucket)
    return buckets


# recursive + cache
@lru_cache
def divide(nums, k):
    if k == 1:
        return [[nums]]
    else:
        ret = []
        for i in range(1, len(nums)):
            for entry in divide(nums[i:], k - 1):
                ret.append([nums[:i], *entry])
        return ret


buckets = divide(nums=[2, 4, 5, 7, 9, 12, 11], k=5)
buckets = divide(nums=list(range(20)), k=10)
# for bucket in buckets:
#     print(bucket)
