from collections import Counter


def delete(counter, total, points=0):
    counter = +counter
    if counter.total() == 0:
        total.append(points)
    points_added = 0
    for num in counter:
        temp = +counter
        points_added = num * temp[num]
        temp[num] = 0
        # if temp[num - 1] == 0 and temp[num + 1] == 0:
        #     continue
        temp[num - 1] = 0
        temp[num + 1] = 0
        delete(temp, total, points + points_added)


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums.sort()
        chunks = []
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if i < len(nums) - 1 and nums[i + 1] - nums[i] <= 1:
                continue
            else:
                chunks.append(temp)
                temp = []
        # print(chunks)
        max_scores = []
        for chunk in chunks:
            print(chunk)
            total = []
            delete(Counter(chunk), total)
            # print(total)
            max_scores.append(max(total))
        return sum(max_scores)


s = Solution()
print(s.deleteAndEarn(nums=[3, 4, 2]))
print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
print(s.deleteAndEarn([3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10]))
print(s.deleteAndEarn([1, 1, 2, 2, 3, 5, 5, 7, 8, 8, 9]))
print(
    s.deleteAndEarn(
        [
            52,
            2,
            43,
            45,
            36,
            56,
            73,
            44,
            23,
            14,
            42,
            82,
            80,
            19,
            61,
            30,
            56,
            83,
            65,
            33,
            14,
            96,
            29,
            5,
            56,
            12,
            82,
            11,
            5,
            52,
            17,
            62,
            65,
            6,
            23,
            14,
            44,
            37,
            19,
            95,
            89,
            44,
            40,
            3,
            44,
            71,
            20,
            13,
            18,
            33,
            83,
            98,
            60,
            74,
            91,
            20,
            11,
            12,
            16,
            79,
            43,
            46,
            71,
            63,
            9,
            84,
            100,
            10,
            14,
            51,
            52,
            66,
            3,
            18,
            54,
            100,
            17,
            85,
            70,
            43,
            4,
            16,
            30,
            58,
            83,
            65,
            53,
            55,
            27,
            28,
            56,
            60,
            53,
            87,
            23,
            30,
            87,
            50,
            80,
            99,
            91,
            4,
            87,
            44,
            28,
            86,
            99,
            88,
            18,
            32,
            77,
            62,
            64,
            15,
            84,
            33,
            23,
            12,
            92,
            72,
            43,
            34,
            54,
            31,
            81,
            5,
            16,
            88,
            11,
            82,
            59,
            87,
            34,
            41,
            60,
            37,
            63,
            39,
            55,
            27,
            27,
            13,
            96,
            22,
            78,
            42,
            59,
            55,
            21,
            98,
            28,
            52,
            63,
            33,
            38,
            5,
            58,
            6,
            8,
            44,
            59,
            40,
            44,
            98,
            82,
            66,
            58,
            6,
            18,
            13,
            25,
            85,
            60,
            100,
            17,
            41,
            52,
            47,
            23,
            94,
            16,
            50,
            62,
            50,
            32,
            97,
            24,
            97,
            45,
            51,
            39,
            32,
            60,
            36,
            66,
            2,
            88,
            38,
            49,
            21,
        ]
    )
)
