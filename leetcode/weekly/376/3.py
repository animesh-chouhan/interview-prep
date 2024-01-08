def closest_palindrome(num):
    # print(num)
    num_list = list(str(num))
    len_num = len(num_list)
    for i in range(len_num // 2):
        num_list[len_num - i - 1] = num_list[i]
    # print(int("".join(num_list)))
    new_num_list = num_list[:]
    if len_num % 2 == 0:
        new_num_list[(len_num // 2) - 1] = str(
            int(new_num_list[(len_num // 2) - 1]) + 1
        )
        new_num_list[len_num // 2] = str(int(new_num_list[len_num // 2]) + 1)
    else:
        new_num_list[len_num // 2] = str(int(new_num_list[len_num // 2]) + 1)
    return [int("".join(num_list)), int("".join(new_num_list))]


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        possible_x = [i for i in range(min_num, max_num + 1) if str(i) == str(i)[::-1]]
        for i in range(min_num, max_num + 1):
            possible_x.extend(closest_palindrome(i))

        # print(possible_x)
        costs = []
        for x in possible_x:
            cost = sum([abs(x - num) for num in nums])
            costs.append(cost)

        print(min(costs))
        return min(costs)


s = Solution()
s.minimumCost(nums=[1, 2, 3, 4, 5])
s.minimumCost(nums=[10, 12, 13, 14, 15])
s.minimumCost(nums=[22, 33, 22, 33, 22])
s.minimumCost([307, 321, 322, 327])
s.minimumCost([102, 103, 105, 106, 109])
s.minimumCost([206, 215, 216, 219, 220, 221])
s.minimumCost(
    [
        123,
        125,
        125,
        123,
        124,
        128,
        128,
        125,
        128,
        128,
        124,
        126,
        127,
        128,
        126,
        127,
        127,
        129,
        127,
        128,
        125,
        128,
        129,
        127,
        123,
        125,
        124,
        123,
        128,
        128,
        125,
        124,
        125,
        128,
        126,
        123,
        128,
        126,
        124,
        128,
        127,
        124,
        129,
        127,
        128,
        129,
        127,
        125,
        127,
        125,
    ]
)

# print(closest_palindrome(221))
