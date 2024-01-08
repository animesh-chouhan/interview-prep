import sys

sys.setrecursionlimit(50000000)


def dist_candy(i, candies, ratings):
    # print(i)
    child_count = len(candies)
    if i < 0 or i > child_count:
        return candies

    left = i - 1
    right = i + 1

    if left >= 0:
        left_candies = candies[left]
        i_candies = candies[i]
        if ratings[left] > ratings[i] and left_candies <= i_candies:
            candies[left] = i_candies + 1
            candies = dist_candy(left, candies, ratings)
        elif ratings[left] < ratings[i] and i_candies <= left_candies:
            candies[i] = left_candies + 1
            candies = dist_candy(i, candies, ratings)

    if right <= child_count - 1:
        right_candies = candies[right]
        i_candies = candies[i]
        if ratings[right] > ratings[i] and right_candies <= i_candies:
            candies[right] = i_candies + 1
            candies = dist_candy(right, candies, ratings)
        elif ratings[right] < ratings[i] and i_candies <= right_candies:
            candies[i] = right_candies + 1
            candies = dist_candy(i, candies, ratings)

    # print(candies)
    return candies


class Solution:
    def candy(self, ratings) -> int:
        candies = [1] * len(ratings)
        dist_candy(0, candies, ratings)


ratings = [5, 2, 4, 0, 1, 3, 2]
candies = [1] * len(ratings)
for i in range(len(candies)):
    candies = dist_candy(i, candies, list(reversed(ratings)))

print(candies)
