from collections import Counter


def get_count_equal(n):
    return pow(2, n) - (n * n + n + 2) // 2


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        counts = []
        total = 0

        c = Counter(nums)
        # print(c)
        if len(c) == 1:
            if c[nums[0]]:
                total += get_count_equal(c[nums[0]])
        else:
            for k in c.keys():
                if c[k] >= 3:
                    total += get_count_equal(c[k])

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    d = nums[j] - nums[i]
                    if d != 0:
                        count = 0
                        prev_i = i
                        next_val = nums[i] + d
                        seq = [nums[i]]
                        mult = []
                        while True:
                            try:
                                # print(i, next_i)
                                next_i = nums.index(next_val, prev_i + 1, len(nums))
                                seq.append(nums[next_i])
                                mult.append(nums[prev_i:next_i].count(nums[prev_i]))
                                prev_i = next_i
                                count += 1
                                next_val += d
                                if count > 1:
                                    total += 1
                                    print(seq, mult, total)

                            except ValueError:
                                mult.append(
                                    nums[prev_i : len(nums)].count(nums[prev_i])
                                )
                                if count > 1:
                                    total += 1
                                    print(seq, mult, total)
                                break

        return total


s = Solution()
# print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8]))
# print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
# print(s.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
print(s.numberOfArithmeticSlices(nums=[2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]))
# print(s.numberOfArithmeticSlices([20, 60, 2, 36, 54, 2, 90, 26, 40]))
# print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
