from collections import Counter


def get_count_equal(n):
    return pow(2, n) - (n * n + n + 2) // 2


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        counts = []
        total = 0

        c = Counter(nums)
        print(c)
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
                        i_count = nums[i:j].count(nums[i])
                        count = 0
                        next_val = nums[j] + d
                        next_i = j
                        seq = [nums[i], nums[j]]
                        while True:
                            try:
                                print(i, next_i)
                                next_i = nums.index(next_val, next_i + 1, len(nums))
                                seq.append(nums[next_i])
                                count += 1
                                next_val += d
                                if count > 0:
                                    total += i_count
                                    print(seq, i_count, total)

                            except ValueError:
                                break

        return total


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        i = 0
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                d = nums[j] - nums[i]
                seq = [nums[i], nums[j]]
                count = 0
                next_i = j
                next_num = nums[j] + d
                while True:
                    try:
                        next_i = nums.index(next_num, next_i + 1, len(nums))
                        # print(next_i)
                        next_num += d
                        count += 1
                        seq.append(nums[next_i])
                        if count > 0:
                            total += nums[next_i:].count(nums[next_i])
                            print(seq, total)

                    except ValueError:
                        break
            i += 1
        return total


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        def next_elem(start_i, d):
            # print(start_i, d)
            next = nums[start_i] + d

            poss_indexes = [i for i in range(start_i + 1, len(nums)) if nums[i] == next]

            if poss_indexes:
                ret = []
                for i in poss_indexes:
                    ret.extend([[nums[start_i]] + k for k in next_elem(i, d)])
                return ret

            return [[nums[start_i]]]

        def next_elem(start_i, d):
            # print(start_i, d)
            next = nums[start_i] + d

            poss_indexes = [i for i in range(start_i + 1, len(nums)) if nums[i] == next]
            try:
                poss_indexes = [nums.index(next, start_i + 1, len(nums))]
            except:
                poss_indexes = []

            if poss_indexes:
                ret = []
                for i in poss_indexes:
                    ret.extend([[start_i] + k for k in next_elem(i, d)])
                return ret

            return [[start_i]]

        total = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = [[nums[i]] + k for k in next_elem(j, nums[j] - nums[i])]
                res = [[i] + k for k in next_elem(j, nums[j] - nums[i])]
                print(res)

                for elem in res:
                    if len(elem) > 2:
                        total += len(elem) - 2

                # print(next_elem(j, nums[j] - nums[i]))
                # for elem in next_elem(i, nums[j] - nums[i]):
                #     print(elem)
        return total


s = Solution()
# print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8]))
print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(s.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
print(s.numberOfArithmeticSlices(nums=[2, 2, 2, 2, 3, 3, 3, 4, 4]))
print(s.numberOfArithmeticSlices([20, 60, 2, 36, 54, 2, 90, 26, 40]))
