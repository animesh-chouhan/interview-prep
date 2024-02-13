from collections import Counter, defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = board
        cols = [[] for _ in board[0]]
        for i in range(len(board[0])):
            for j in range(len(board)):
                cols[i].append(board[j][i])

        # print(rows)
        # print(cols)

        threex3 = [[] for _ in range(9)]
        k = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                [threex3[k].extend(e[j : j + 3]) for e in rows[i : i + 3]]
                k += 1

        # print(threex3)

        def check(grid):
            for item in grid:
                c = Counter(item)
                for i in range(1, 10):
                    if c[str(i)] > 1:
                        return False
            return True

        return all([check(rows), check(cols), check(threex3)])


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = board
        cols = [[] for _ in board[0]]
        for i in range(len(board[0])):
            for j in range(len(board)):
                cols[i].append(board[j][i])

        # print(rows)
        # print(cols)

        threex3 = [[] for _ in range(9)]
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                [threex3[i + j // 3].extend(e[j : j + 3]) for e in rows[i : i + 3]]

        print(threex3)

        def check(grid):
            for item in grid:
                c = Counter(item)
                for i in range(1, 10):
                    if c[str(i)] > 1:
                        return False
            return True

        return all([check(rows), check(cols), check(threex3)])


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem == ".":
                    continue
                else:
                    if (
                        elem in rows[i]
                        or elem in cols[j]
                        or elem in squares[(i // 3, j // 3)]
                    ):
                        return False
                    else:
                        rows[i].append(elem)
                        cols[j].append(elem)
                        squares[(i // 3, j // 3)].append(elem)

        # print(rows)
        # print(cols)
        # print(squares)
        return True


def get3x3(board):
    ret = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            k = 3 * (i // 3) + j // 3
            ret[k].append(board[i][j])
    for s in ret:
        print(s)


s = Solution()
print(
    s.isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(s.isValidSudoku(board))
get3x3(board)
